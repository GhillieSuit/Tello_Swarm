@echo off

REM connect to tello black and make it connect to tello-dev wifi

    netsh wlan connect TELLO-D3CF56
    timeout /t 10
    PacketSender\packetsender -u -a 192.168.10.1 8889 command
    timeout /t 2
    PacketSender\packetsender -u -a 192.168.10.1 8889 "ap telloswarm 12345678"
    timeout /t 1


REM connect to tello black and make it connect to tello-dev wifi

    netsh wlan connect TELLO-D8D990
    timeout /t 10
    PacketSender\packetsender -u -a 192.168.10.1 8889 command
    timeout /t 2
    PacketSender\packetsender -u -a 192.168.10.1 8889 "ap telloswarm 12345678"
    timeout /t 1


REM connect to tello black and make it connect to tello-dev wifi

    netsh wlan connect TELLO-DC95A1
    timeout /t 10
    PacketSender\packetsender -u -a 192.168.10.1 8889 command
    timeout /t 2
    PacketSender\packetsender -u -a 192.168.10.1 8889 "ap telloswarm 12345678"
    timeout /t 1


REM connect to tello black and make it connect to tello-dev wifi

    netsh wlan connect TELLO-DC959D
    timeout /t 10
    PacketSender\packetsender -u -a 192.168.10.1 8889 command
    timeout /t 2
    PacketSender\packetsender -u -a 192.168.10.1 8889 "ap telloswarm 12345678"
    timeout /t 1


REM connect to tello black and make it connect to tello-dev wifi

    netsh wlan connect TELLO-D8DEE5
    timeout /t 10
    PacketSender\packetsender -u -a 192.168.10.1 8889 command
    timeout /t 2
    PacketSender\packetsender -u -a 192.168.10.1 8889 "ap telloswarm 12345678"
    timeout /t 1


