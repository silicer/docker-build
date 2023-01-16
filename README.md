<!--
 * @Author: Silicer
 * @Date: 2021-07-30 19:10:06
 * @Description:
 * @LastEditors: Silicer
 * @LastEditTime: 2021-08-10 09:38:02
-->

利用 `Github Actions` 自动构建 Docker 镜像并上传到 Docker Hub 。

本仓库于每隔4小时自动检测更新并构建如下镜像：

- [Tsuk1ko/cq-picsearcher-bot](https://github.com/Tsuk1ko/cq-picsearcher-bot)
- [Quan666/ELF_RSS](https://github.com/Quan666/ELF_RSS)
- [caddyserver/caddy](https://github.com/caddyserver/caddy)(带`replace-response`和`caddy2-filter`插件)
- [Mrs4s/go-cqhttp](https://github.com/Mrs4s/go-cqhttp)
