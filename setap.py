from tkinter import *
import tkinter.font
import tkinter.scrolledtext as tkst

class AP_Setting:
    def __init__(self, parent):
        font_main = tkinter.font.Font(family="맑은 고딕", size=14)
        font_text = tkinter.font.Font(family="맑은 고딕", size=12)    
        
        top = self.top = Toplevel(parent)
        top.geometry('215x190')

        try:
            with open(r'res\temp\ap.txt', 'r') as f:
                self.temp = f.readlines()
                self.ssid = self.temp[0].rstrip('\n')
                self.password = self.temp[1].rstrip('\n')
        except FileNotFoundError:
            print('file not found error')
            with open(r'res\temp\ap.txt', 'w') as f:
                f.write('ssid\npassword')
        except:
            print('file open error')
            with open(r'res\temp\ap.txt', 'w') as f:
                f.write('ssid\npassword')
        
        Label(top, text="SSID", font=font_main).place(x=15, y=15)
        self.e1 = Entry(top, font=font_text)
        self.e1.insert(END, self.ssid)
        self.e1.place(x=15, y=40)
        
        Label(top, text="Password", font=font_main).place(x=15, y=70)
        self.e2 = Entry(top, font=font_text)
        self.e2.insert(END, self.password)
        self.e2.place(x=15, y=95)

        b = Button(top, text="OK", font=font_text, command=self.ok)
        b.pack(side='bottom', padx=15, pady=15, fill='x')

    def ok(self):
        self.ssid = self.e1.get()
        self.password = self.e2.get()
        with open(r'res\temp\ap.txt', 'w') as f:
            f.write(self.ssid + '\n' + self.password)
        self.top.destroy()

    def get(self):
        try:
            with open(r'res\temp\ap.txt', 'r') as f:
                self.temp = f.readlines()
                self.ssid = self.temp[0].rstrip('\n')
                self.password = self.temp[1].rstrip('\n')
        except FileNotFoundError:
            print('file not found error')
            with open(r'res\temp\ap.txt', 'w') as f:
                f.write('ssid\npassword')
        except:
            print('file open error')
            with open(r'res\temp\ap.txt', 'w') as f:
                f.write('ssid\npassword')
        return self.ssid, self.password

    ssid = 'ssid'
    password = 'password'

    try:
        with open(r'res\temp\ap.txt', 'r') as f:
            temp = f.readlines()
            ssid = temp[0].rstrip('\n')
            password = temp[1].rstrip('\n')
    except FileNotFoundError:
        with open(r'res\temp\ap.txt', 'w') as f:
            f.write("ssid\npassword")
    except:
        with open(r'res\temp\ap.txt', 'w') as f:
            f.write("ssid\npassword")



class edit_connecting:
    def __init__(self, parent):
        font_main = tkinter.font.Font(family="맑은 고딕", size=14)
        font_text = tkinter.font.Font(family="맑은 고딕", size=12)    
        
        top = self.top = Toplevel(parent)
        top.geometry('215x430')

        Label(top, text="List", font=font_main).place(x=15, y=15)
        self.t1 = tkst.ScrolledText(top, font=font_text)
        self.t1.place(x=15, y=50, width=185, height=320)

        try:
            with open(r'res\temp\drone.txt', 'r') as f:
                self.temp = f.readlines()
        except FileNotFoundError:
            print('file not found error')
            with open(r'res\temp\drone.txt', 'w') as f:
                f.write('')
        except:
            print('file open error')
            with open(r'res\temp\drone.txt', 'w') as f:
                f.write('')
        self.t1.insert(END, ''.join(self.temp))

        b = Button(top, text="Apply", font=font_text, command=self.ok)
        b.pack(side='bottom', padx=15, pady=15, fill='x')

    def ok(self):
        with open(r'res\temp\drone.txt', 'w') as f:
            text_temp = self.t1.get(1.0,END).splitlines()
            text = ''
            for idx in text_temp:
                if idx == '':
                    pass
                else:
                    text += idx+'\n'
            f.write(text)
        with open(r'res\temp\drone.txt', 'r') as f:
            self.temp = f.readlines()
        self.t1.delete(1.0, END)    
        self.t1.insert(END, ''.join(self.temp))
        self.top.destroy()

    def get(self):
        with open(r'res\temp\drone.txt', 'r') as f:
            self.temp = f.readlines()
        return self.temp
    
    temp = ''
    
    try:
        with open(r'res\temp\drone.txt', 'r') as f:
            temp = f.readlines()
    except FileNotFoundError:
        print('file not found error')
        with open(r'res\temp\drone.txt', 'w') as f:
            f.write('')
    except:
        print('file open error')
        with open(r'res\temp\drone.txt', 'w') as f:
            f.write('')


