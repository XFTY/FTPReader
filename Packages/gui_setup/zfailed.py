import tkinter
from tkinter.ttk import *
import zinfo

class failedui(tkinter.Tk):
    def __init__(self, errcode=None) -> None:
        super().__init__()
        self.width = 1024
        self.height = 512
        self.left = (self.winfo_screenwidth() - self.width) / 2
        self.top = (self.winfo_screenheight() - self.height) / 2
        self.geometry("{}x{}+{}+{}".format(int(self.width),int(self.height),int(self.left),int(self.top)))
        self.resizable(False,False)
        self.title("FTPReader - v{}".format(zinfo.__version__))
        self.LeftCanvas = tkinter.Canvas(self,bg='#272727',height=512,width=300)
        self.LeftCanvas.pack(side='left')
        self.titlel = Label(self,text=zinfo.title + "Failed",font=('Arial',20))
        self.titlel.place(x=310,y=10)
        self.faildlav = Label(self, text="由于以下原因，FTPReader")
        self.mainloop()
        
if __name__ == "__main__":
    failedui()