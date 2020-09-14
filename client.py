import socket
S=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
S.connect(("127.0.0.1",5000))
while True:
    data = "CLIENT =>" + input("")
    S.send(bytes(data,encoding='utf-8'))
    print(S.recv(1024))