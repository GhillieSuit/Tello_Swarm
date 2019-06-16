# -*- coding: UTF-8 -*-
import tello
import textbox
import scan
import threading
import cv2
import numpy as np
import time
import tkinter.scrolledtext as tkst
import tkinter.font
from tkinter import *
from PIL import Image, ImageTk

chk_refresh = True

def refresh():
    global chk_refresh
    if chk_refresh == False:
        return
    chk_refresh = False
    textbox.set_log('Scanning . . . .')
    lbx_drone.delete('0','end')
    
    scan_thread = threading.Thread(target=tello.scan_conn)
    scan_thread.start()
    
    src = cv2.imread(r"res\img\refresh.png", cv2.IMREAD_COLOR)
    
    height, width, channel = src.shape

    for i in range(0,361):
        matrix = cv2.getRotationMatrix2D((width/2, height/2), -i, 1)
        dst = cv2.warpAffine(src, matrix, (width, height))

        img = ImageTk.PhotoImage(Image.fromarray(dst))
        btn_refresh.configure(image=img)
        btn_refresh.image=img
        root.update()
        time.sleep(0.015)
    refresh_list()
    chk_refresh = True


def refresh_list():
    tello.set_list(lbx_drone)


def press_refresh(event):
    refresh()


def focus_out(event):
    if (event.y > 30):
        root.focus()


def click_left(event):
    if event.x > 75 and event.x < 125:
        if event.y > 10 and event.y < 60:
            tello.trust_up(spn_trust.get())
        elif event.y > 140 and event.y < 190:
            tello.trust_down(spn_trust.get())
    elif event.y > 75 and event.y < 125:
        if event.x > 10 and event.x < 60:
            tello.yaw_ccw(spn_yaw.get())
        elif event.x > 140 and event.x < 190:
            tello.yaw_cw(spn_yaw.get())

    
def click_right(event):   
    if event.x > 75 and event.x < 125:
        if event.y > 10 and event.y < 60:
            tello.pitch_front(spn_pitch.get())
        elif event.y > 140 and event.y < 190:
            tello.pitch_back(spn_pitch.get())
    elif event.y > 75 and event.y < 125:
        if event.x > 10 and event.x < 60:
            tello.roll_left(spn_roll.get())
        elif event.x > 140 and event.x < 190:
            tello.roll_right(spn_roll.get())


def bind_key(event):
    if (event.widget == tbx_cmd or event.widget == tbx_log):
        return
    elif event.keysym == 'F5':
        refresh()
    elif event.keysym == 'w':
        tello.trust_up(spn_trust.get())
    elif event.keysym == 's':
        tello.trust_down(spn_trust.get())
    elif event.keysym == 'a':
        tello.yaw_ccw(spn_yaw.get())   
    elif event.keysym == 'd':
        tello.yaw_cw(spn_yaw.get())
    elif event.keysym == 'Up':
        tello.pitch_front(spn_pitch.get())
    elif event.keysym == 'Down':
        tello.pitch_back(spn_pitch.get())
    elif event.keysym == 'Left':
        tello.roll_left(spn_roll.get())   
    elif event.keysym == 'Right':
        tello.roll_right(spn_roll.get())
    elif event.keysym == 'r':
        spn_trust.set(spn_trust.get()+10)
    elif event.keysym == 'f':
        spn_trust.set(spn_trust.get()-10)
    elif event.keysym == 'q':
        spn_yaw.set(spn_yaw.get()-15)    
    elif event.keysym == 'e':
        spn_yaw.set(spn_yaw.get()+15)
    elif event.keysym == 'bracketleft':
        spn_pitch.set(spn_pitch.get()-10)
    elif event.keysym == 'bracketright':
        spn_pitch.set(spn_pitch.get()+10)
    elif event.keysym == 'comma':
        spn_roll.set(spn_roll.get()-10)
    elif event.keysym == 'period':
        spn_roll.set(spn_roll.get()+10)
    elif event.keysym == 'F1':
        tello.takeoff()
    elif event.keysym == 'F2':
        tello.land()
    elif event.keysym == 'h':
        tello.flip_l()
    elif event.keysym == 'j':
        tello.flip_b()
    elif event.keysym == 'k':
        tello.flip_f()
    elif event.keysym == 'l':
        tello.flip_r()


def send_cmd(event):
    str_cmd = tbx_cmd.get()
    if(str_cmd == ''):
        return
    tbx_cmd.delete(0, 'end')
    tello.sendto(str_cmd)


def press_cmd():
    send_cmd(None)


def onselect(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    #print('Selected item %d: "%s"' % (index, value))
    temp = value.split(' ')
    w.delete(index)
    if temp[0] == '●':
        w.insert(index, '○ '+temp[1])
    elif temp[0] == '○':
        w.insert(index, '● '+temp[1])
    tello.get_list(lbx_drone)
    

# create main_frame
root = Tk()
root.geometry("1280x720")
root.resizable(False, False)
root.title("Drone Swarm")
root.wm_iconbitmap('res\img\icon.ico')
root.bind('<Button-1>', focus_out)
root.bind('<Key>', bind_key)


# create font
font_main = tkinter.font.Font(family="맑은 고딕", size=14)
font_text = tkinter.font.Font(family="맑은 고딕", size=12)


# image load
img_refresh = PhotoImage(file=r'res\img\refresh.png')
img_left = PhotoImage(file=r'res\img\controller_left.png')
img_right = PhotoImage(file=r'res\img\controller_right.png')
img_takeoff = PhotoImage(file=r'res\img\takeoff.png')
img_land = PhotoImage(file=r'res\img\land.png')
img_flip_f = PhotoImage(file=r'res\img\flip_f.png')
img_flip_b = PhotoImage(file=r'res\img\flip_b.png')
img_flip_l = PhotoImage(file=r'res\img\flip_l.png')
img_flip_r = PhotoImage(file=r'res\img\flip_r.png')


# create object
lbl_title = Label(root, text='Drone List', font=font_main)
btn_refresh = Button(root, image=img_refresh, bg='white', command=refresh)
lbx_drone = Listbox(root, font=font_text)
lbx_drone.bind('<<ListboxSelect>>', onselect)

lbl_left = Label(root, image=img_left)
lbl_left.bind('<Button-1>', click_left)
var_trust = IntVar()
spn_trust = Scale(root, variable=var_trust, orient=VERTICAL, showvalue=0, from_=500, to=20)
lbl_trust = Label(root, textvariable=var_trust, font=font_text)
var_yaw = IntVar()
spn_yaw = Scale(root, variable=var_yaw, orient=HORIZONTAL, showvalue=0, from_=15, to=720)
lbl_yaw = Label(root, textvariable=var_yaw, anchor='w', font=font_text)

lbl_right = Label(root, image=img_right)
lbl_right.bind('<Button-1>', click_right)
var_pitch = IntVar()
spn_pitch = Scale(root, variable=var_pitch, orient=VERTICAL, showvalue=0, from_=500, to=20)
lbl_pitch = Label(root, textvariable=var_pitch, font=font_text)
var_roll = IntVar()
spn_roll = Scale(root, variable=var_roll, orient=HORIZONTAL, showvalue=0, from_=20, to=500)
lbl_roll = Label(root, textvariable=var_roll, anchor='e', font=font_text)

lbl_log = Label(root, text='Consol Log', font=font_main)
tbx_log = tkst.ScrolledText(root, font=font_text)
tbx_log.bind("<Key>", lambda e: "break")
tbx_box = Entry(root, font=font_text)
tbx_cmd = Entry(root, font=font_text)
tbx_cmd.bind('<Return>', send_cmd)
lbl_cmd = Label(root, text='cmd>', font=font_text, bg='white')
btn_cmd = Button(root, text='Send', font=font_text, bg='white', command=press_cmd)


lbl_conn = Label(root, text='Connect AP', font=font_main)
btn_conn = Button(root, text='1. AP Setting', font=font_text, command=lambda: scan.set_ap(root))
btn_edit = Button(root, text='2. Edit Connect', font=font_text, command=lambda: scan.edit_text(root))
btn_bat = Button(root, text='3. Edit Batch', font=font_text, command=scan.edit_bat)
btn_run = Button(root, text='4. Run Batch', font=font_text, command=scan.run_bat)

lbl_scen = Label(root, text='Scenario', font=font_main)
btn_scen = Button(root, text='Run Scenario', font=font_text, command=lambda: scan.open_scen(root))

lbl_flight = Label(root, text='Flight Mode', font=font_main)
btn_takeoff = Button(root, image=img_takeoff, bg='white', command=tello.takeoff)
btn_land = Button(root, image=img_land, bg='white', command=tello.land)
lbl_takeoff = Label(root, text='Take off')
lbl_land = Label(root, text='Land')

lbl_flip = Label(root, text='Flip', font=font_main)
btn_flip_l = Button(root, image=img_flip_l, bg='white')
btn_flip_b = Button(root, image=img_flip_b, bg='white')
btn_flip_f = Button(root, image=img_flip_f, bg='white')
btn_flip_r = Button(root, image=img_flip_r, bg='white')
lbl_flip_l = Label(root, text='Left')
lbl_flip_b = Label(root, text='Back')
lbl_flip_f = Label(root, text='Front')
lbl_flip_r = Label(root, text='Right')


# set object
lbl_title.place(x=17, y=15, width=100, height=30)
btn_refresh.place(x=175, y=12, width=36, height=36)
lbx_drone.place(x=15, y=50, width=200, height=655)

lbl_left.place(x=280, y=430, width=200, height=200)
spn_trust.place(x=245, y=450, height=180)
lbl_trust.place(x=239, y=430, width=35)
spn_yaw.place(x=275, y=640, width=170)
lbl_yaw.place(x=445, y=635, width=30)

lbl_right.place(x=665, y=430, width=200, height=200)
spn_pitch.place(x=880, y=450, height=180)
lbl_pitch.place(x=873, y=430, width=35)
spn_roll.place(x=695, y=640, width=170)
lbl_roll.place(x=665, y=635, width=30)

lbl_log.place(x=247, y=15)
tbx_log.place(x=245, y=50, width=656, height=369)
tbx_box.place(x=245, y=675, width=600, height=30)
tbx_cmd.place(x=294, y=675, width=551, height=30)
lbl_cmd.place(x=246, y=676)
btn_cmd.place(x=850, y=672)

lbl_conn.place(x=933, y=15)
btn_conn.place(x=931, y=50, width=332, height=45)
btn_edit.place(x=931, y=105, width=332, height=45)
btn_bat.place(x=931, y=160, width=332, height=45)
btn_run.place(x=931, y=215, width=332, height=45)

lbl_scen.place(x=933, y=280)
btn_scen.place(x=931, y=310, width=332, height=45)

lbl_flight.place(x=933, y=420)
btn_takeoff.place(x=933, y=455, width=60, height=60)
btn_land.place(x=1022, y=455, width=60, height=60)
lbl_takeoff.place(x=933, y=515, width=60)
lbl_land.place(x=1022, y=515, width=60)

lbl_flip.place(x=933, y=565)
btn_flip_l.place(x=933, y=600, width=60, height=60)
btn_flip_b.place(x=1022, y=600, width=60, height=60)
btn_flip_f.place(x=1112, y=600, width=60, height=60)
btn_flip_r.place(x=1202, y=600, width=60, height=60)
lbl_flip_l.place(x=933, y=660, width=60)
lbl_flip_b.place(x=1022, y=660, width=60)
lbl_flip_f.place(x=1112, y=660, width=60)
lbl_flip_r.place(x=1202, y=660, width=60)


# set values default
spn_trust.set(50)
spn_yaw.set(90)
spn_pitch.set(50)
spn_roll.set(50)
tbx_log.insert(END, 'Program Start')

textbox.set_logbox(tbx_log)

root.mainloop()
