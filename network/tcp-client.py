# 客户端
import socket
# 创建一个socket:
# AF_INET指定使用IPv4协议
# SOCK_STREAM指定使用面向流的TCP协议
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 建立连接:
s.connect(('www.sina.com.cn', 80))
# 向新浪服务器发送请求
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# 客户端必须先发请求给服务器，服务器收到后才发数据给客户端

buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

# close
s.close()

print(data)

header, html = data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
with open('sina.html', 'wb') as f:
    f.write(html)

# 测试tcp-server.py
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 建立连接:
sock.connect(('127.0.0.1',9000))
# 接收欢迎消息:
print(sock.recv(1024).decode('utf-8'))
# 发送消息
for data in [b'Michael', b'Tracy', b'Sarah']:
    sock.send(data)
    print(sock.recv(1024).decode('utf-8'))

sock.send(b'exit')
sock.close()
