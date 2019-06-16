import threading 
import socket
import sys
import time
import platform  

host = ''
port = 9000
locaddr = (host,port) 

tello_address = []

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

sock.bind(locaddr)

chk = 0

def recv():
    while True: 
        try:
            #data, server = sock.recvfrom(1518)
            data, server = sock.recvfrom(1024)
            print(str(server[0]) + " : " + data.decode(encoding="utf-8"))
            if(data.decode(encoding="utf-8") == 'ok' and chk == 0):
                tello_address.append(tuple(server))
        except Exception:
            print ('\nExit . . .\n')
            break

#recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()


chkip = 3
while(True):
    if(chkip >= 30):
        break
    else:
        print("send 'command' to 192.168.0."+str(chkip))
        sock.sendto('command'.encode(encoding="utf-8"), ('192.168.0.'+str(chkip),8889))
    chkip += 1
"""
print("send 'command' to 192.168.0.* via broadcast")
sock.sendto('command'.encode(encoding="utf-8"), ('<broadcast>',8889))
"""

time.sleep(5)
print('drone list')
for i in tello_address:
    print(i)
chk = 1

print ('Readed to fly!')

while True: 
    try:
        python_version = str(platform.python_version())
        version_init_num = int(python_version.partition('.')[0]) 
       # print (version_init_num)
        if version_init_num == 3:
            msg = input("");
        elif version_init_num == 2:
            msg = raw_input("");
        
        if not msg:
            break  

        if 'end' in msg:
            print ('...')
            sock.close()  
            break

        # Send data
        msg = msg.encode(encoding="utf-8") 
        for i in tello_address:
            sent = sock.sendto(msg, tuple(i))

    except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()  
        break



