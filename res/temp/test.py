import threading
import time
import socket
import tkinter as tk


def recv_conn():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('',9000))
    tello_address.clear()
    while True:
        try:
            sock.settimeout(10)
            data, server = sock.recvfrom(1024)
            sock.settimeout(None)
            print(str(server[0]) + " : " + data.decode(encoding="utf-8"))
            if(data.decode(encoding="utf-8") == 'ok'):
                print(server)
                tello_address.append(tuple(server))
        except socket.timeout:
            print('Thread Time Out')
            break
        except Exception:
            print ('Recv Error')
            break
    sock.close()


def scan_conn():
    global localhost
    chk = True
    conn_recvThread = threading.Thread(target=recv_conn)
    conn_recvThread.start()
    chkip = 2
    while chkip < 255:
        chkip += 1
        if localhost == '192.168.0.'+str(chkip):
            continue
        conn_sock.sendto('command'.encode(encoding="utf-8"), ('192.168.0.'+str(chkip),8889))  
        

def set_list(listbox):
    listbox.delete('0','end')
    for addr in tello_address:
        listbox.insert('end', '● ' + addr[0])



def trust_up(e = None):
    print("Trust up")


def trust_down(e = None):
    print("Trust down")


def yaw_cw(e = None):
    print("Yaw cw")


def yaw_ccw(e = None):
    print("Yaw ccw")


def pitch_front(e = None):
    print("Pitch front")

    
def pitch_back(e = None):
    print("Pitch back")


def roll_left(e = None):
    print("Roll left")

    
def roll_right(e = None):
    print("Roll right")



tello_address = []

conn_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
conn_sock.connect(("192.168.0.0", 80))
localhost = conn_sock.getsockname()[0]
print('localhost :',localhost)
