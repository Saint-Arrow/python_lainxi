import os, time


ip="192.168.13.159"
t=0
output_dir=".\\output_"+ip

def mkdir(path):
    # 引入模块
    import os
 
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
 
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
 
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path) 
 
        print (path+' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print (path+' 目录已存在')
        return False

import socket
import struct
import binascii

def udp_sendmsg(ip,port,str):
    client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    ip_port = (ip, port)
    str2=binascii.unhexlify(str)
    client.sendto(str2,ip_port)

def time_wait(timeout):
    while 1==1:
        time.sleep(1)
        timeout=timeout-1
        if timeout == 0:
            return 
        else:
            print(timeout,"s...")

#os.system(r'start /d"D:\upgrade v2.8" upgrade.exe')
path = os.path.dirname(__file__)
os.chdir(path)
mkdir(output_dir)



while 1==1:
    os.system(r'ffmpeg -f gdigrab -framerate 10 -i desktop -frames:v 1 -y '+output_dir+'\\'+str(t)+'.jpg')
    t=t+1
    time.sleep(2)
    
    udp_sendmsg(ip,1259,'8101040002ff')
    time_wait(60)



