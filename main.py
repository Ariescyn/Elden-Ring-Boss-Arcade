from tkinter import *
from PIL import Image, ImageTk

appname = "EldenRing Boss Arcade"


def donothing():
    pass



class App(Tk):
    def __init__(self):
        super().__init__()
        self.title(appname)
        self.geometry("400x400")

        # BUILD MENUBAR
        menubar = Menu(self)
        self.config(menu=menubar)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Import Save File", command=donothing)
        filemenu.add_command(label="seamless Co-op Mode", command=donothing)
        filemenu.add_separator()
        filemenu.add_command(label="Force quit EldenRing", command=lambda:do(self))
        filemenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        bg_img = ImageTk.PhotoImage(image=Image.open("./data/icons/Astel-TJWM.ico"))
        background = Label(self, image=bg_img)

        background.place(x=-200,y=33)




class Popup:
    def __init__(self, parent_window, buttons=False):

        popupwin = Toplevel(parent_window)
        popupwin.title("ERBA")
        # popupwin.geometry("200x75")
        lab = Label(popupwin, text="hdhawdwahd")
        lab.grid(row=0, column=0, padx=30, pady=30)
        # Places popup window at center of the root window
        x = parent_window.winfo_x()
        y = parent_window.winfo_y()
        popupwin.geometry("+%d+%d" % (x + 200, y + 200))

        if buttons:
            but_yes = Button(popupwin,text='YES',borderwidth=5,width=6,command=donothing)
            but_yes.grid(row=1, column=0, padx=(0, 0), pady=(0, 0))


def do(rootwin):
    x = Popup(rootwin)









if __name__ == "__main__":
    app = App()
    app.mainloop()
