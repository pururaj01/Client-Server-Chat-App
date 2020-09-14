import socket
S=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
S.bind(("127.0.0.1",5000))
S.listen(5)
con,addr=S.accept()
print(addr)
while True:
    data = "SERVER=>" + input(" ")
    con.send(bytes(data,encoding="utf-8"))
    print(con.recv(1024))