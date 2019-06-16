from tkinter import *
import tkinter.font
import tkinter.scrolledtext as tkst
import tkinter.messagebox


class Scenario:
    def __init__(self, parent):
        font_main = tkinter.font.Font(family="맑은 고딕", size=14)
        font_text = tkinter.font.Font(family="맑은 고딕", size=12)    
        
        top = self.top = Toplevel(parent)
        top.geometry('230x400')

        Label(top, text="Scenario List", font=font_main).place(x=15, y=15)
        self.lbx_scen = Listbox(top, font=font_text)
        self.lbx_scen.insert(0, 'asdf')
        self.lbx_scen.insert(1, 'qwer')
        #self.lbx_scen.bind('<<ListboxSelect>>', self.onselect)
        self.lbx_scen.place(x=15, y=40, width=200, height=300)

        b = Button(top, text="Run", font=font_text, command=self.ok)
        b.pack(side='bottom', padx=15, pady=15, fill='x')


    def ok(self):
        try:
            w = self.lbx_scen
            index = int(w.curselection()[0])
            value = w.get(index)
            d = play(self.top, value)
            #self.top.destroy()
        except:
            tkinter.messagebox.showerror('Select Error','시나리오를 선택하세요.')


    def onselect(a, evt):
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)


class play:
    def __init__(self, parent, text):
        font_main = tkinter.font.Font(family="맑은 고딕", size=14)
        font_text = tkinter.font.Font(family="맑은 고딕", size=12)    
        
        top = self.top = Toplevel(parent)
        top.geometry('240x125')
        
        img_play = PhotoImage(file=r'res\img\play.png')
        img_pause = PhotoImage(file=r'res\img\pause.png')
        img_stop = PhotoImage(file=r'res\img\stop.png')
        
        Label(top, text=text, font=font_main).place(x=15, y=15)
        
        self.btn_play = Button(top, image=img_play, bg='white')
        self.btn_play.image = img_play
        self.btn_play.place(x=15, y=50, width=60, height=60)
        
        self.btn_pause = Button(top, image=img_pause, bg='white')
        self.btn_pause.image = img_pause
        self.btn_pause.place(x=90, y=50, width=60, height=60)
        
        self.btn_stop = Button(top, image=img_stop, bg='white')
        self.btn_stop.image = img_stop
        self.btn_stop.place(x=165, y=50, width=60, height=60)     
