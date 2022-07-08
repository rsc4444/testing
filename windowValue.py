from tkinter import *
from tkinter.ttk import *
import random
import sys

root = Tk()
root.title("delta X")

def deltaX():
    try:
        r = random.randint(-259,-250)
        print(r)
        lbl.config(text = r)
        lbl.after(1000, deltaX)
    # except KeyboardInterrupt:
    #     print("KeyboardInterrupt")
    #     sys.exit("EXIT KI")
    except:
        print("Unerwarteter Fehler")
        sys.exit("EXIT UE")

lbl = Label(root, font = ("calibri", 40, "bold"),background = "black",foreground = "white")
lbl.pack(anchor = "center")
deltaX()
mainloop()
