import setap
import test
import subprocess


def set_ap(root):
    d = setap.AP_Setting(root)

def edit_ap():
    ssid, password = setap.AP_Setting.get(setap.AP_Setting)
    ap = ssid + ' ' + password
    return ap

def edit_bat():
    temp = setap.edit_connecting.get(setap.edit_connecting)
    print(temp)
    str1 = """REM connect to tello black and make it connect to tello-dev wifi

    netsh wlan connect """
    str2 = """    timeout /t 10
    PacketSender\packetsender -u -a 192.168.10.1 8889 command
    timeout /t 2
    PacketSender\packetsender -u -a 192.168.10.1 8889 "ap """ + edit_ap() + """"
    timeout /t 1\n\n\n"""
    stdstr = ''
    for name in temp:    
        text = 'ssid='
        text += name
        text += ' name='
        text += name
        stdstr += str1
        stdstr += name
        stdstr += str2
    print(stdstr)
    with open(r'res\temp\conn_drone.bat', 'w') as f:
        f.write("@echo off\n\n")
    with open(r'res\temp\conn_drone.bat', 'a') as f:
        f.write(stdstr)

        
def edit_text(root):
    d = setap.edit_connecting(root)

def run_bat():
    subprocess.call([r'res\temp\conn_drone.bat'])

def open_scen(root):
    d = test.Scenario(root)


