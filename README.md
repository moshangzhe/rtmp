# RTMP服务器搭建&实时视频直播
## 使用Docker搭建rtmp服务器
安装docker:
`curl -sSL https://get.daocloud.io/docker | sh`

拉取rtmp镜像:
`docker pull jun3/rtmp`

运行rtmp服务器:
`docker run --name rtmp -p 1935:1935 -p 8080:80 -d -it jun3/rtmp`

在浏览器中输入:(ip):8080/stat可以查看后台
![1](https://github.com/moshangzhe/rtmp/blob/master/picture/1.jpg)