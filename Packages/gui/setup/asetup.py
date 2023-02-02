# -*- coding:utf-8 -*-

#breakpoint()

import getpass
import os
import sys
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from typing import *
import zinfo
import beula

#import init_sittings

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
        self.forwho = Label(self.root,text='配置端')
        self.notes = Label(self.root,text='由A.S.C Workgroup提供源代码，详情请前往 https://www.github.com/XFTY')
        self.notes2 = Label(self.root,text='项目仍在公测中，软件可能不稳定，如果您发现了软件的bug，可以上传到github的issue页面反馈。')
        self.copyright1 = Label(self.root,text='版权所有：A.S.C Team，保留所有权利。')
        self.welcome_title = Label(self.root,text='欢迎使用！',font=('simhei',20))
        self.vie = Label(self.root, text="若要继续，请点击'下一步'。")

        self.cancel_button = Button(self.root,text='  退出安装程序  ',command=self.exit)
        self.go_next_button = Button(self.root,text='下一步',command=self.go_next1)

        self.leftlabel = Label(self.root,text='目录:',foreground='white',background='#272727', font=('simhei', 15))
        self.leftlabel.place(x=10,y=10)
        self.leftlabel2 = Label(self.root, text="欢迎界面", foreground="white", background="#272727")
        self.leftlabel2.place(x=40, y=40)

        self.LeftCanvas.pack(side='left') 
        self.title.place(x=310,y=10)
        self.versiontitle.place(x=310,y=50)
        self.forwho.place(x=310,y=70)
        self.notes.place(x=310,y=110)
        self.notes2.place(x=310,y=130)
        self.copyright1.place(x=310,y=170)
        self.leftlabel.place(x=10,y=self.x_way)
        self.go_next_button.place(x=900,y=480)
        
        self.welcome_title.place(x=310,y=210)
        self.vie.place(x=310, y=250)
        self.cancel_button.place(x=310,y=480)
        
        self.root.protocol("WM_DELETE_WINDOW",self.exit)

        self.root.mainloop()
    
    def cancel(self):
        print('user cancel exit code:0')
        sys.exit(0)

    def go_next1(self) -> NoReturn:
        '''
        
        '''

        '''
        self.versiontitle.place_forget()
        self.forwho.place_forget()
        self.notes.place_forget()
        self.notes2.place_forget()
        self.copyright1.place_forget()
        self.welcome_title.place_forget()
        self.go_next_button.configure(command=self.go_next2)
        '''
        self.root.destroy()
        beula.eula2()
        sys.exit(0)


    def go_next2(self):
        print(1)

    def exit(self):
        if messagebox.askquestion('退出','确定退出？') == 'yes':
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
