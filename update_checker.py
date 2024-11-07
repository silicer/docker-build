import os
import yaml
import requests
import subprocess
import feedparser

def get_latest_version(project):
    check_type = project['check_type']
    repo_url = project['repo_url']

    if check_type == 'github_release':
        api_url = repo_url.replace('https://github.com/', 'https://api.github.com/repos/') + '/releases/latest'
        response = requests.get(api_url)
        data = response.json()
        return data.get('tag_name')

    elif check_type == 'git_commit':
        repo_name = repo_url.split('/')[-1]
        clone_path = os.path.join('repos', project['name'])
        if not os.path.exists(clone_path):
            subprocess.run(['git', 'clone', repo_url, clone_path])
        else:
            subprocess.run(['git', '-C', clone_path, 'pull'])
        latest_commit = subprocess.check_output(['git', '-C', clone_path, 'log', '-1', '--pretty=format:%H']).decode('utf-8')
        return latest_commit

    elif check_type == 'rss_feed':
        feed = feedparser.parse(repo_url)
        if feed.entries:
            latest_entry = feed.entries[0]
            version_name = latest_entry.title
            download_link = latest_entry.guid
            return (version_name, download_link)
        else:
            print(f"No entries found in RSS feed for {project['name']}")
            return None

    else:
        print(f"Unknown check_type {check_type}")
        return None

def trigger_dispatch_event(project: dict, version):
    token = os.environ['ACTIONS_TRIGGER']
    event_type = project['event_type']
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {token}'
    }
    repo = os.environ['GITHUB_REPOSITORY']
    api_url = f'https://api.github.com/repos/{repo}/dispatches'    

    if isinstance(version, tuple):
        payload = {'apk': version[0], 'dlLink': version[1]}
    else:
        payload = {
            'name': project['name'],
            'platforms': "linux/amd64" if project.get('platforms', None) == None else project['platforms'],
            'repo': project['repo_url'],
            'version': version,
            'latest': "true" if project.get('latest', None) == None else str(project['latest']).lower(),
            'prefix': project['prefix'],
            'suffix': project['suffix']
        }

    data = {
        'event_type': event_type,
        'client_payload': payload
    }

    response = requests.post(api_url, headers=headers, json=data)
    if response.status_code == 204:
        print(f"Successfully dispatched event {event_type}")
    else:
        print(f"Failed to dispatch event {event_type}: {response.status_code} {response.text}")

def main():
    with open('projects.yaml', 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    projects = config['projects']

    for project in projects:
        if project['enabled'] == False:
            continue
        name = project['name']
        print(f"Processing project {name}")
        latest_version = get_latest_version(project)

        if latest_version is None:
            print(f"Could not get latest version for {name}")
            continue

        if isinstance(latest_version, tuple):
            version_identifier = latest_version[0]
        else:
            version_identifier = latest_version

        version_file = os.path.join(name, 'version')
        if os.path.exists(version_file):
            with open(version_file, 'r') as vf:
                last_version = vf.read().strip()
        else:
            last_version = None

        if version_identifier != last_version:
            print(f"New version detected for {name}: {version_identifier}")
            with open(version_file, 'w') as vf:
                vf.write(version_identifier)
            trigger_dispatch_event(project, latest_version)
        else:
            print(f"No new version for {name}")

if __name__ == '__main__':
    main()
