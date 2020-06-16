from socket import socket
from pyautogui import size, moveTo

sock = socket()
w, h = size()
sock.connect((input('IP Address Server Has Messaged You: '), int(input('Port Server Has Messaged You: '))))
sock.send(f'{w}x{h}'.encode())
while True:
    msg = sock.recv(1024).decode()
    if msg == 'exit':
        sock.close()
        quit()
    exec(msg)
    sock.send(b'7 Bytes')