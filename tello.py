import threading
import time
import socket
import tkinter as tk
import textbox

bool_recv = True
cmd_count = 0

def recv():
    global bool_recv, cmd_count
    while True:
        while bool_recv:
            try:
                conn_sock.settimeout(5)
                data, server = conn_sock.recvfrom(1024)
                conn_sock.settimeout(None)
                textbox.set_log(str(server[0]) + " : " + data.decode(encoding="utf-8"))
                if data == 'error' or data == 'error Not joystick':
                    conn_sock.sendto(tello_command[server].encode(encoding="utf-8"), server)
                    textbox.set_log('Resend to '  + str(server[0]) + ' : ' + str(tello_command[server]))
                else:
                    tello_command[server] = ''
                    cmd_count -= 1
                    print(cmd_count)
            except socket.timeout:
                print('timeout')
                for key, var in tello_command.items():
                    if var != '':
                        conn_sock.sendto(var.encode(encoding="utf-8"), key)
                        textbox.set_log('Resend to ' + key[0] + ' : ' + var)
                cmd_count = 0           
            except Exception:
                textbox.set_log('Recv Error')
        time.sleep(1)

      
def recv_conn():
    global bool_recv, cmd_count
    bool_recv = False
    tello_address.clear()
    tello_command = {}
    while True:
        try:
            conn_sock.settimeout(5)
            data, server = conn_sock.recvfrom(1024)
            conn_sock.settimeout(None)
            textbox.set_log(str(server[0]) + " : " + data.decode(encoding="utf-8"))
            if(data.decode(encoding="utf-8") == 'ok'):
                print(server)
                tello_address.append(tuple(server))
                tello_command = {tuple(server):''}
        except socket.timeout:
            textbox.set_log('End Scanning !')
            break
        except Exception:
            textbox.set_log('Recv Error')
            break
    cmd_count = 0
    bool_recv = True


def scan_conn():
    global localhost
    conn_recvThread = threading.Thread(target=recv_conn)
    conn_recvThread.start()
    chk = True
    chkip = 2
    time.sleep(1)
    while chkip < 255:
        chkip += 1
        if localhost == '192.168.0.'+str(chkip):
            continue
        conn_sock.sendto('command'.encode(encoding="utf-8"), ('192.168.0.'+str(chkip),8889))  


def set_list(listbox):
    listbox.delete('0','end')
    tello_address.sort()
    for addr in tello_address:
        listbox.insert('end', '● ' + addr[0])


def get_list(listbox):
    tello_address.clear()
    for idx in range(listbox.size()):
        print(str(listbox.get(idx)))
        temp = str(listbox.get(idx)).split(' ')
        if temp[0] ==  '●':
            tello_address.append((temp[1],8889))


def sendto(msg):
    global cmd_count
    textbox.set_log(msg)
    for addr in tello_address:
        conn_sock.sendto(msg.encode(encoding="utf-8"), addr)
        print(cmd_count)
        print('send ' + msg + ' to ' + str(addr))


def trust_up(h, e = None):
    msg = 'up ' + str(h)
    sendto(msg)
    

def trust_down(h, e = None):
    msg = 'down ' + str(h)
    sendto(msg)


def yaw_cw(h, e = None):
    msg = 'cw ' + str(h)
    sendto(msg)


def yaw_ccw(h, e = None):
    msg = 'ccw ' + str(h)
    sendto(msg)


def pitch_front(h, e = None):
    msg = 'forward ' + str(h)
    sendto(msg)

    
def pitch_back(h, e = None):
    msg = 'back ' + str(h)
    sendto(msg)


def roll_left(h, e = None):
    msg = 'left ' + str(h)
    sendto(msg)
    
    
def roll_right(h, e = None):
    msg = 'right ' + str(h)
    sendto(msg)


def takeoff(e = None):
    msg = 'takeoff'
    sendto(msg)
    

def land(e = None):
    msg = 'land'
    sendto(msg)


def flip_f(e = None):
    msg = 'flip f'
    sendto(msg)


def flip_b(e = None):
    msg = 'flip b'
    sendto(msg)


def flip_l(e = None):
    msg = 'flip l'
    sendto(msg)


def flip_r(e = None):
    msg = 'flip r'
    sendto(msg)


def get_sock():
    return conn_sock


def get_addr_list():
    return tello_address


tello_address = []
tello_command = {}

test_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
test_sock.connect(("192.168.0.0", 80))
localhost = test_sock.getsockname()[0]
print('localhost :',localhost)
test_sock.close()
    
conn_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
conn_sock.bind(('',9000))
print('create conn_sock')

recvThread = threading.Thread(target=recv)
recvThread.start()
print('recv thread start')
