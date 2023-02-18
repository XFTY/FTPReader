# -*- coding:utf-8 -*-

#breakpoint()

import getpass
import os
# print(os.getcwd())
import sys
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from typing import *
import zinfo
import beula
import json

#import init_sittings

with open("lang/default.json", "r") as f:
    cache = f.read()
    langcache = json.loads(cache)
    try:
        with open("lang/{}/asetup.json".format(langcache["default"]), "r", encoding="utf-8") as f1:
            lang = f1.read()
            lang = json.loads(lang)
    except Exception as e:
        messagebox.showerror("error", "There was an error before loading the language file\nCannot found this file:\n{}".format(e))
        sys.exit()


__version__ = zinfo.__version__

try:
    f = open("C:\\Users\\{}\\Documents\\FTPReader\\config.ftpconf".format(getpass.getuser()),'r+')
    conf = f.read()
    f.close()
    is_first_use = False
    if conf == '':
        is_first_use = True
except Exception:
    os.mkdir("C:\\Users\\{}\\Documents\\FTPReader".format(getpass.getuser()))
    f = open("C:\\Users\\{}\\Documents\\FTPReader\\config.ftpconf".format(getpass.getuser()),'w+')
    f.close()
    is_first_use = True

class welcomegui():
    def __init__(self,*args,**kwargs) -> NoReturn:
        self.root = Tk()
        #self.root = root
        self.width = 1024
        self.height = 512
        self.x_way = 10
        self.left = (self.root.winfo_screenwidth() - self.width) / 2
        self.top = (self.root.winfo_screenheight() - self.height) / 2

    def guiset(self):
        '''
        GUI界面初始化设置
        ------

        GUI初始界面设置
        '''
        self.root.geometry("{}x{}+{}+{}".format(int(self.width),int(self.height),int(self.left),int(self.top)))
        self.root.resizable(False,False)
        self.root.title("FTPReader - v{}".format(__version__))

        self.LeftCanvas = Canvas(self.root,bg='#272727',height=512,width=300)
        self.title = Label(self.root,text=zinfo.title + "Welcome",font=('Arial',20))

        #第一阶段GUI界面
        self.first_list = [None,'self.versiontitle']
        self.versiontitle = Label(self.root,text=f'version:{__version__}',font=('Arial',10)) # 显示版本信息
        try:
            self.forwho = Label(self.root,text=lang["forwho"])
            self.notes = Label(self.root,text=lang["notes"])
            self.notes2 = Label(self.root,text=lang["notes2"])
            self.copyright1 = Label(self.root,text=lang["copyright1"])
            self.lang_tra = Label(self.root, text=lang["lang_tra"])
            self.welcome_title = Label(self.root,text=lang["welcome_title"],font=('simhei',20))
            self.vie = Label(self.root, text=lang["vie"])

            self.cancel_button = Button(self.root,text=lang["cancel_button"],command=self.exit)
            self.go_next_button = Button(self.root,text=lang["go_next_button"],command=self.go_next1)

            self.leftlabel = Label(self.root,text=lang["leftlabel"],foreground='white',background='#272727', font=('simhei', 15))
            self.leftlabel.place(x=10,y=10)
            self.leftlabel2 = Label(self.root, text=lang["leftlabel2"], foreground="white", background="#272727")
            self.leftlabel2.place(x=40, y=40)
        except KeyError as e:
            messagebox.showerror("error", "There was an error before loading the language file\nSome key is lost, please check it\nlostkey: {}".format(e))
        self.LeftCanvas.pack(side='left') 
        self.lang_tra.place(x=310, y=190)
        self.title.place(x=310,y=10)
        self.versiontitle.place(x=310,y=50)
        self.forwho.place(x=310,y=70)
        self.notes.place(x=310,y=110)
        self.notes2.place(x=310,y=130)
        self.copyright1.place(x=310,y=170)
        self.leftlabel.place(x=10,y=self.x_way)
        self.go_next_button.place(x=900,y=480)
        
        self.welcome_title.place(x=310,y=230)
        self.vie.place(x=310, y=270)
        self.cancel_button.place(x=310,y=480)
        
        self.root.protocol("WM_DELETE_WINDOW",self.exit)

        self.root.mainloop()
    
    def cancel(self):
        print('user cancel exit code:0')
        sys.exit(0)

    def go_next1(self) -> NoReturn:
        self.root.destroy()
        beula.eula2()
        sys.exit(0)


    def go_next2(self):
        print(1)

    def exit(self):
        if messagebox.askquestion('exit','exit？') == 'yes':
            os.system("rmdir /s/q C:\\Users\\{}\\Documents\\FTPReader".format(getpass.getuser()))
            sys.exit(0)



        

def start()->...:
    '''
    start this main gui
    '''
    obj = welcomegui()
    obj.guiset()


if __name__ == '__main__':
    start()
    #breakpoint()
