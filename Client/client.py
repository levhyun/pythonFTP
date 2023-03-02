import ftplib
import os

def check_file(name):
    path = "./"
    for (root, directories, files) in os.walk(path):
        for file in files:
            if '.txt' in file:
                file_path = os.path.join(root, file)
                if f'./{name}.txt' == file_path:
                    return True

def get_files():
    List = []
    path = "./"
    for (root, directories, files) in os.walk(path):
        for file in files:
            if '.txt' in file:
                file_path = os.path.join(root, file)
                List.append(file_path)
    return List

def addr_set(address):
    addr = ''
    port = ''
    for i in range(0, len(address)-1):
        if address[i] == ':':
            addr = address[:i]
            port = address[i+1:]
            return addr, port

user_name = str(input('Enter a server user name > '))
user_pswd = str(input('Enter a server user password > '))
server_address = str(input('Enter a server address > '))

ip, port = addr_set(server_address)

ftp = ftplib.FTP()
ftp.connect(ip,int(port))
ftp.login(user_name,user_pswd)

while True:
    print('[file list]')
    files = get_files()
    for file in files:
        print(file)

    name = input('Enter a sendfile name > ')
    send = check_file(name)

    if send == True:
        file_name = f"{name}.txt"
        os.chdir(r"./")

        file = open("./" + file_name,'rb')
        ftp.storbinary("STOR " + file_name, file)
        file.close()
        ftp.close

        print(f'send file : {file_name}\n')
    else:
        print(f'[ERROR] File does not exist\n')