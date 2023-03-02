import socket
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def get_address():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("pwnbit.kr", 443))
    return sock.getsockname()[0]

user_name = str(input('Enter a user name > '))
user_pswd = str(input('Enter a user password > '))

ip = get_address()
port = 2023
print(f'server address : {ip}:{port}')

authorizer = DummyAuthorizer()
authorizer.add_user(user_name, user_pswd, "./recvFiles", perm="elradfmw")
authorizer.add_anonymous("./recvFiles", perm="elradfmw")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer((ip,port), handler)
server.serve_forever()