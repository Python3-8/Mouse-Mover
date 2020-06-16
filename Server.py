from socket import socket, AF_INET, SOCK_DGRAM
from pyautogui import size, position
from random import randint
_ = socket(AF_INET, SOCK_DGRAM)
_.connect(('8.8.8.8', 8080))
ip = _.getsockname()[0]
_.close()
sock = socket()
port_found = False
w, h = size()
print('\nBinding Port...')
while not port_found:
    port = randint(8000, 10000)
    try:
        sock.bind(('', port))
        port_found = True
    except:
        pass
print('Binding Finsihed Successfully With Port', str(port) + '.')
print('Please Message \'' + ip, '|', str(port) + '\' to The Client.')
print('Waiting For Incoming Connections...\n')
sock.listen(1)
conn, add = sock.accept()
print(f'{add[0]} has Connected to the Server!')
client_w, client_h = conn.recv(1024).decode().split('x')
client_w, client_h = float(client_w), float(client_h)
while True:
    x, y = position()
    if x and y:
        ratio = (x / w, y / h)
        msg = f'moveTo({ratio[0] * client_w}, {ratio[1] * client_h}, 0.01)'.encode()
    else:
        msg = b'exit'
    conn.send(msg)
    conn.recv(1024)
    if msg == b'exit':
        conn.close()
        sock.close()
        quit()
