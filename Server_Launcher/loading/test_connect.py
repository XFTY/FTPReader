import socket
# 创建客户端套接字
sk = socket.socket()           
# 尝试连接服务器
sk.connect(('127.0.0.1',8080))
while True:
    # 信息发送
    info = input('>>>')
    sk.send(bytes(info,encoding='utf-8'))
    # 信息接收
    ret = sk.recv(1024)
    # 结束会话
    if ret == b'bye':
        sk.send(b'bye')
        break
    # 信息打印
    print(ret.decode('utf-8'))
# 关闭客户端套接字
sk.close() 