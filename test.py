from tkinter import *
import tkinter.font
import tkinter.scrolledtext as tkst
import tkinter.messagebox
import time
import threading
import socket
import os
import tello
import textbox


class Scenario:
    def __init__(self, parent):
        font_main = tkinter.font.Font(family="맑은 고딕", size=14)
        font_text = tkinter.font.Font(family="맑은 고딕", size=12)    
        
        top = self.top = Toplevel(parent)
        top.geometry('230x400')

        Label(top, text="Scenario List", font=font_main).place(x=15, y=15)
        self.lbx_scen = Listbox(top, font=font_text)
        #self.lbx_scen.bind('<<ListboxSelect>>', self.onselect)
        self.lbx_scen.place(x=15, y=40, width=200, height=300)

        b = Button(top, text="Run", font=font_text, command=self.ok)
        b.pack(side='bottom', padx=15, pady=15, fill='x')
        self.search("scenario")


    def ok(self):
        """try:
            w = self.lbx_scen
            index = int(w.curselection()[0])
            value = w.get(index)
            d = play(self.top, value)
            #self.top.destroy()
        except:
            tkinter.messagebox.showerror('Select Error','시나리오를 선택하세요.')
"""
        w = self.lbx_scen
        index = int(w.curselection()[0])
        value = w.get(index)
        d = play(self.top, value)

    def search(self, dirname):
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            ext = os.path.splitext(full_filename)[-1]
            if ext == '.txt':
                f_name = full_filename.split('\\')[-1]
                self.lbx_scen.insert(END, f_name)


    def onselect(a, evt):
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)


class play:
    chk_play = False
    chk_pause = False
    chk_stop = False
    
    def __init__(self, parent, text):
        font_main = tkinter.font.Font(family="맑은 고딕", size=14)
        font_text = tkinter.font.Font(family="맑은 고딕", size=12)    
        
        top = self.top = Toplevel(parent)
        top.geometry('240x125')
        
        img_play = PhotoImage(file=r'res\img\play.png')
        img_pause = PhotoImage(file=r'res\img\pause.png')
        img_stop = PhotoImage(file=r'res\img\stop.png')
        
        Label(top, text=text, font=font_main).place(x=15, y=15)
        
        self.btn_play = Button(top, image=img_play, bg='white', command=lambda: self.play('scenario\\'+text))
        self.btn_play.image = img_play
        self.btn_play.place(x=15, y=50, width=60, height=60)
        
        self.btn_pause = Button(top, image=img_pause, bg='white', command=self.pause)
        self.btn_pause.image = img_pause
        self.btn_pause.place(x=90, y=50, width=60, height=60)
        
        self.btn_stop = Button(top, image=img_stop, bg='white', command=self.stop)
        self.btn_stop.image = img_stop
        self.btn_stop.place(x=165, y=50, width=60, height=60)


    def play(self, file_name):
        if self.chk_play:
            if self.chk_pause:
                self.pause()
            return
        self.chk_play = True
        threading.Thread(target=lambda: self.play_scen(file_name)).start()


    def play_scen(self, file_name):
        conn_sock = tello.get_sock()
        tello_address = tello.get_addr_list()
        
        f = open(file_name, "r")
        commands = f.readlines()

        for command in commands:
            while self.chk_pause and not self.chk_stop:
                pass
            if self.chk_stop:
                self.chk_stop = False
                self.chk_play = False
                self.chk_pause = False
                for tello_addr in tello_address:
                    conn_sock.sendto('land'.encode(encoding="utf-8"), tello_addr)
                    tello.tello_command[tello_addr] = 'land'
                    tello.cmd_count += 1
                    print(tello.cmd_count)
                    
                return
            if command != '' and command != '\n':
                command = command.rstrip()

                if command.find('delay') != -1:
                    sec = float(command.partition('delay')[2])
                    textbox.set_log('delay ' + str(sec))
                    time.sleep(sec)
                    pass
                else:
                    addr = command.split(' ')[0]
                    try:
                        cmd = command.split(' ')[1] + " " + command.split(' ')[2]
                    except:
                        cmd = command.split(' ')[1]
                    finally:
                        textbox.set_log(cmd)
                    if addr == '*':
                        for tello_addr in tello_address:
                            conn_sock.sendto(cmd.encode(encoding="utf-8"), tello_addr)
                            tello.tello_command[tello_addr] = cmd
                            tello.cmd_count += 1
                            print(tello.cmd_count)
                    else:
                        t_addr = int(addr)
                        conn_sock.sendto(cmd.encode(encoding="utf-8"), tello_address[t_addr - 1])
                        tello.tello_command[tello_address[t_addr - 1]] = cmd
                        tello.cmd_count += 1
                        print(tello.cmd_count)
        self.chk_play = False
        

    def pause(self):
        if not self.chk_play:
            return
        if not self.chk_pause:
            textbox.set_log('pause')
        else:
            textbox.set_log('continue')
        self.chk_pause = not self.chk_pause


    def stop(self):
        textbox.set_log('stop')
        self.chk_stop = True




