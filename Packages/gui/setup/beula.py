import getpass
import os
import sys
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from typing import *
import zinfo

__version__ = zinfo.__version__

class eula2(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.width = 1024
        self.height = 512
        self.left = (self.winfo_screenwidth() - self.width) / 2
        self.top = (self.winfo_screenheight() - self.height) / 2
        self.geometry("{}x{}+{}+{}".format(int(self.width),int(self.height),int(self.left),int(self.top)))
        self.resizable(False,False)
        self.title("FTPReader - v{}".format(__version__))
        self.LeftCanvas = Canvas(self,bg='#272727',height=512,width=300)
        self.LeftCanvas.pack(side='left')
        self.protocol("WM_DELETE_WINDOW",self.exit)

        self.title = Label(self,text=zinfo.title + "EULA",font=('Arial',20))
        self.title.place(x=310,y=10)

        self.versiontitle = Label(self,text=f'version:{__version__}',font=('Arial',10)) # 显示版本信息
        self.forwho = Label(self,text='配置端')
        self.versiontitle.place(x=310,y=50)
        self.forwho.place(x=310,y=70)

        self.eulatitle = Label(self, text="开源软件用户许可条款", font=("simhei", 20))
        self.eulatitle.place(x=310, y=100)

        self.eulainfolabel = Label(self, text="请认真阅读本许可条款，如果您同意，请点击'我同意许可条款'")
        self.eulainfolabel.place(x=310, y=140)

        self.agreebutton = Button(self, text="我同意许可条款")

        self.leftlabel = Label(self,text='目录:',foreground='white',background='#272727', font=('simhei', 15))
        self.leftlabel.place(x=10,y=10)
        self.leftlabel2 = Label(self, text="欢迎界面", foreground="green", background="#272727")
        self.leftlabel2.place(x=40, y=40)
        self.titleeula = Label(self, text="用户许可条款", foreground="white", background="#272727")
        self.titleeula.place(x=40, y=80)

        self.mainloop()
    def exit(self):
        if messagebox.askquestion('退出','确定退出？') == 'yes':
            sys.exit(0)


if __name__ == "__main__":
    eula2()