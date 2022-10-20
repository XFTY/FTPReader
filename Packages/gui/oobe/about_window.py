from distutils.command.config import LANG_EXT
from tkinter import *
from tkinter.ttk import *
import webbrowser
import os
#from tkinter.tix import *

__version__ = 'AE1909'
name = 'FTPReader'


class about_window():
    def __init__(self) -> None:
        super().__init__()
        self.root = Tk()
        self.width = 618
        self.height = 496
        self.x_way = 10
        self.left = (self.root.winfo_screenwidth() - self.width) / 2
        self.top = (self.root.winfo_screenheight() - self.height) / 2
        self.GNU_GPL = open(f"{os.getcwd()}\LICENSE",'r',encoding='utf-8')
        self.GNU_GPL_read = self.GNU_GPL.read()
        self.GNU_GPL.close()
        self.EULA = open(f"{os.getcwd()}\LICENSE",'r',encoding='utf-8')
        self.EULA_read = self.EULA.read()
        self.EULA.close()
    
    def gui(self):
        self.root.title(f'FTPReader {__version__} Professional')
        self.root.geometry("{}x{}+{}+{}".format(int(self.width),int(self.height),int(self.left),int(self.top)))
        self.root.resizable(False,False)
        self.about_window_canvas()
        self.root.mainloop()

    def about_window_canvas(self):
        self.title = Label(self.root,text='FTPReader',font=('Arial',20)).place(x=230,y=10)
        self.title_gnu = Label(self.root,text='本软件受GNU_GPL协议保护').place(x=20,y=50)
        self.gnu = Text(self.root,width=80,height=10,undo=True)
        self.gnu.insert(END,self.GNU_GPL_read)
        self.gnu.place(x=20,y=70)
        self.name = Label(self.root,text=f'软件名称：{name}').place(x=20,y=250.1)
        self.ver = Label(self.root,text=f'版本：{__version__}(内测版)').place(x=20,y=270)
        self.aia = Label(self.root,text='开发者：XFTY').place(x=20,y=290)
        self.iai = Label(self.root,text='©XFTY, 保留所有权利。').place(x=20,y=320)
        self.list = Label(self.root,text='根据').place(x=20,y=340)
        self.button = Button(self.root,text='FTPReader使用条款',command=self.run).place(x=60,y=340)
        self.lists = Label(self.root,text=', 您允许使用本产品。').place(x=190,y=340)

    def run(self):
        webbrowser.open('https://github.com/XFTY/FTPReader/blob/main/EULA.txt')


def run():
    obj = about_window()
    obj.gui()

if __name__ == '__main__':
    run()