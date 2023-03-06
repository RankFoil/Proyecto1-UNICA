from tkinter import *
import usr
raiz=Tk()
raiz.title("Máquina Expendedora")
raiz.resizable(0,0)
raiz.geometry("400x650")
b1=Frame()
b1.pack()
b1.config(cursor="hand2")
#Label(b1, text="1").place(x=14,y=7)
Button(b1,text="1",command=Usuario.press()).pack()

raiz.mainloop()
