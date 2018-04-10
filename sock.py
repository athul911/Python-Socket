import socket
import time
socketc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socketd=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
th='www.facebook.com'
th1='www.google.com'
tp=80
socketc.connect((th,tp))
socketd.connect((th1,tp))
socketd.send("GET /HTTP/1.1\r \n HOST:www.google.com \r \n")
time.sleep(10)
socketc.send("GET /HTTP/1.1\r \n HOST:www.facebook.com \r \n")
res1=socketd.recv(2048)
res=socketc.recv(2048)
print res
time.sleep(4)
print res1
