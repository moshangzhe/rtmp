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

##编写视频推流代码
###1.使用ffmpeg实现rtmp推流

测试ffmpeg:

`ffmpeg -f video4linux2 -s  640x480 -i /dev/video10  -vcodec libx264 -preset:v ultrafast -tune:v zerolatency -f flv rtmp://`

###2.在python中实现ffmpeg

(1)使用python-opencv采集摄像头数据

使用`cv.VideoCapture(0)`打开摄像头。

使用`cap.read()`获取图像。

将图像编码成字符串格式:`frame.tostring()`

(2)使用subprocess模块运行ffmpeg软件。

subprocess能够在子线程中运行软件，并且连接到他们的输入输出。

`self.command = []`设置了FFmpeg命令文本。

使用`subprocess.Popen()`方法运行FFmpeg命令并将视频数据传入输入管道中。

