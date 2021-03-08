import cv2 as cv
import time
import subprocess as sp
import psutil
import time


class RTMP:
    def __init__(self, rtmp_url=None):  # 类实例化的时候传入rtmp地址和帧传入队列
        self.rtmp_url = rtmp_url
        fps = 30  # 设置帧速率
        # 设置分辨率
        width = 640  # 宽
        height = 480  # 高

        # 设置FFmpeg命令文本
        self.command = ['ffmpeg',
                        '-y',
                        '-f', 'rawvideo',
                        '-vcodec', 'rawvideo',
                        '-pix_fmt', 'bgr24',
                        '-s', "{}x{}".format(width, height),
                        '-r', str(fps),
                        '-i', '-',
                        '-c:v', 'libx264',
                        '-pix_fmt', 'yuv420p',
                        '-preset', 'ultrafast',
                        '-tune', 'zerolatency',
                        '-f', 'flv',
                        self.rtmp_url]

    # 向服务器推送
    def push_frame(self):
        cap = cv.VideoCapture(-1)
        _, frame = cap.read()
        # 指定在哪些cpu核上运行。我的ARM有6核，前4核较慢做辅助处理。后2核较快，做核心程序的处理。这里指定推流动作在慢的4个核中运行
        p = psutil.Process()
        p.cpu_affinity([0, 1, 2, 3])
        # 配置向os传递命令的管道
        p = sp.Popen(self.command, stdin=sp.PIPE)

        while True:
            _, frame = cap.read()
            p.stdin.write(frame.tostring())
            time.sleep(0.05)


if __name__ == '__main__':
    rtmpUrl = "rtmp://116.62.153.244:1935/stream/wx2"
    my_pusher = RTMP(rtmp_url=rtmpUrl)
    my_pusher.push_frame()
