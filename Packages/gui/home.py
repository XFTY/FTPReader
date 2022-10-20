from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import webbrowser
import oobe.about_window

__version__ = 'AE1909'

class homegui():
    def __init__(self) -> None:
        self.home = Tk()
        self.width = 1024
        self.height = 512
        self.x_way = 10
        self.left = (self.home.winfo_screenwidth() - self.width) / 2
        self.top = (self.home.winfo_screenheight() - self.height) / 2
    
    def guiset(self):
        self.home.title(f'FTPReader {__version__} Professional')
        self.home.geometry("{}x{}+{}+{}".format(int(self.width),int(self.height),int(self.left),int(self.top)))
        self.home.resizable(False,False)
        self.menu_set()
        self.home.mainloop()

    def menu_set(self):
        self.aboutmenu = Menu(self.home,tearoff=0)
        self.aboutmenu.add_command(label='about FTPReader',command=oobe.about_window.run)

        self.feedback_menu = Menu(self.home,tearoff=0)
        self.feedback_menu.add_command(label='反馈一个bug     ',command=self.feedback_goto)
        self.feedback_menu.add_command(label='反馈一个软件故障代码     ',command=self.feedback_goto)
        self.feedback_menu.add_command(label='反馈其他问题     ',command=self.feedback_goto)


        self.topmenu = Menu(self.home,tearoff=False)
        self.topmenu.add_cascade(label='FTPReader')
        self.topmenu.add_cascade(label='设置')
        self.topmenu.add_cascade(label='帮助')
        self.topmenu.add_cascade(label='反馈',menu=self.feedback_menu)
        self.topmenu.add_cascade(label='关于',menu=self.aboutmenu)
        self.home.config(menu=self.topmenu)

    def about_ftpreader(self):
        messagebox.showinfo('关于FTPReader',f'FTPReader\nversion:{__version__}\n本软件收GNU-GPL协议保护')
    
    def feedback_goto(self):
        if messagebox.askquestion('打开链接','即将打开以下链接：   \nhttps://github.com/XFTY/FTPReader/issues \n您稍后可以在这个网页反馈\n您确定吗？') == 'yes':
            webbrowser.open('https://github.com/XFTY/FTPReader/issues')

def start():
    '''
    start this main gui
    '''
    obj = homegui()
    obj.guiset()

start()