from tkinter import *


def set_logbox(Text):
    global tbx_log
    tbx_log = Text


def set_log(msg):
    global tbx_log
    print(msg)
    tbx_log.insert(END, '\n'+msg)
    tbx_log.see(END)


tbx_log = None;
