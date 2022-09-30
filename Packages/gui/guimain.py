# -*- coding:utf-8 -*-

from tkinter import *
from tkinter.ttk import *
import os
import getpass
import __future__# If you use python2.6+

__version__ = '1.8-pre-release'


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
    def __init__(self,root) -> None:
        self.root = root
        self.width = 1024
        self.height = 512
        self.x_way = 10
        self.left = (self.root.winfo_screenwidth() - self.width) / 2
        self.top = (self.root.winfo_screenheight() - self.height) / 2

    def guiset(self):
        self.root.geometry("{}x{}+{}+{}".format(int(self.width),int(self.height),int(self.left),int(self.top)))
        self.root.resizable(False,False)
        self.root.title("FTPReader - v{}".format(__version__))

        self.LeftCanvas = Canvas(self.root,bg='#272727',height=512,width=300)
        self.title = Label(self.root,text='FTPReader - Your program is always on call',font=('Arial',20))
        self.versiontitle = Label(self.root,text=f'version:{__version__}',font=('Arial',10))
        self.forwho = Label(self.root,text='配置端')
        self.notes = Label(self.root,text='由XFTY提供源代码，详情请前往 https://www.github.com/XFTY')
        self.notes2 = Label(self.root,text='项目仍在公测中，软件可能不稳定，如果您发现了软件的bug，可以上传到github的issue页面反馈。')
        self.copyright1 = Label(self.root,text='版权所有：XFTY，保留所有权利。')
        self.welcome_title = Label(self.root,text='欢迎使用！',font=('simhei',20))

        self.leftlabel = Label(self.root,text='等待用户的反应......',foreground='white',background='#272727')

        self.LeftCanvas.pack(side='left') 
        self.title.place(x=310,y=10)
        self.versiontitle.place(x=310,y=50)
        self.forwho.place(x=310,y=70)
        self.notes.place(x=310,y=110)
        self.notes2.place(x=310,y=130)
        self.copyright1.place(x=310,y=170)
        self.leftlabel.place(x=10,y=self.x_way)
        if is_first_use:
           self.welcome_title.place(x=310,y=210)

def start()->...:
    '''
    start this main gui
    '''
    root = Tk()
    obj = welcomegui(root)
    obj.guiset()
    root.mainloop()

if __name__ == '__main__':
    start()