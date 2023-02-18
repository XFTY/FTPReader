import sys
import tkinter
from tkinter import messagebox
import tkinter.ttk
import zinfo
import json

__version__ = zinfo.__version__

class eula2(tkinter.Tk):
    def __init__(self) -> None:
        super().__init__()
        # self.columnconfigure(0, weight=1)
        self.lang = self.__readjson()
        self.license = self.__readlicense()
        self.menu = self.__readjsonmenu()
        self.width = 1024
        self.height = 512
        self.left = (self.winfo_screenwidth() - self.width) / 2
        self.top = (self.winfo_screenheight() - self.height) / 2
        self.geometry("{}x{}+{}+{}".format(int(self.width),int(self.height),int(self.left),int(self.top)))
        self.resizable(False,False)
        self.title("FTPReader - v{}".format(__version__))
        self.LeftCanvas = tkinter.Canvas(self,bg='#272727',height=512,width=300)
        self.LeftCanvas.pack(side='left')
        self.protocol("WM_DELETE_WINDOW",self.exit)

        self.title = tkinter.ttk.Label(self,text=zinfo.title + "EULA",font=('Arial',20))
        self.title.place(x=310,y=10)

        try:
            self.versiontitle = tkinter.ttk.Label(self,text=f'version:{__version__}',font=('Arial',10)) # 显示版本信息
            self.forwho = tkinter.ttk.Label(self,text=self.lang["forwho"])
            self.versiontitle.place(x=310,y=50)
            self.forwho.place(x=310,y=70)

            self.eulatitle = tkinter.ttk.Label(self, text=self.lang["eulatitle"], font=("simhei", 20))
            self.eulatitle.place(x=310, y=100)

            self.eulainfolabel = tkinter.ttk.Label(self, text=self.lang["eulatitlelabel"])
            self.eulainfolabel.place(x=310, y=140)

            self.leftlabel = tkinter.ttk.Label(self,text=self.menu["menutitle"],foreground='white',background='#272727', font=('simhei', 15))
            self.leftlabel.place(x=10,y=10)
            self.leftlabel2 = tkinter.ttk.Label(self, text=self.menu["menu1"], foreground="green", background="#272727")
            self.leftlabel2.place(x=40, y=40)
            self.titleeula = tkinter.ttk.Label(self, text=self.menu["menu2"], foreground="white", background="#272727")
            self.titleeula.place(x=40, y=80)
            
            self.scroolbar = tkinter.ttk.Scrollbar(self, orient=tkinter.VERTICAL)
            self.textlabel = tkinter.Text(self, width=70, height=15, undo=True, yscrollcommand=self.scroolbar)
            self.textlabel.insert(tkinter.INSERT, self.license)
            self.scroolbar.config(command=self.textlabel.yview)
            self.textlabel.place(x=310, y=200)
            self.textlabel.configure(state="disabled")
            # self.scroolbar.place(x=800, y=300)
            self.scroolbar.pack(fill="y", side="right")

            self.RadioButton_IntVar = tkinter.IntVar()
            self.RadioButton_IntVar.set(1)
            self.RadioButton_AgreeButton = tkinter.ttk.Radiobutton(self, text=self.lang["agreenRadiobutton"], variable=self.RadioButton_IntVar, value=0)
            self.RadioButton_NotAgreeButton = tkinter.ttk.Radiobutton(self, text=self.lang["noagreeRadiobutton"], variable=self.RadioButton_IntVar, value=1)
            self.RadioButton_AgreeButton.place(x=310, y=400)
            self.RadioButton_NotAgreeButton.place(x=310, y=420)

            self.go_next_button = tkinter.ttk.Button(self, text=self.lang["gonextbutton"], command=self.go_next)
            self.go_next_button.place(x=900, y=480)
        
        except KeyError as e:
            messagebox.showerror("error", "There was an error before loading the language file\nSome key are lost, please check it\nlostkey: {}".format(e))
            sys.exit(-1)

        self.mainloop()

    def exit(self):
        if messagebox.askquestion('exit','exit?') == 'yes':
            sys.exit(0)
    
    def __readjson(self) -> list:
        with open("lang/default.json", "r", encoding="utf-8") as f:
            cache1 = json.loads(f.read())
            with open("lang/{}/beula.json".format(cache1["default"]), "r", encoding="utf-8") as f1:
                return json.loads(f1.read())

    def __readjsonmenu(self) -> list:
        with open("lang/zh-CN/menu.json", "r", encoding="utf-8") as f:
            return json.loads(f.read())

    def __readlicense(self) -> str:
        with open("lang/LICENSE", "r", encoding="utf-8") as f:
            return f.read()
    
    def go_next(self):
        if self.RadioButton_IntVar.get() == 1:
            messagebox.showwarning("FTPReader - EULA Warning", "Pleace agree EULA!                         ")

if __name__ == "__main__":
    eula2()