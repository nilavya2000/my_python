from tkinter import *

window=Tk()

def km_miles():
    print(e1_value.get())
    t1.insert(END,e1_value.get())

b1=Button(window,text='execute',command=km_miles)
b1.grid(row=0,column=1)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=3,column=1)
t1=Text(window,width=20)
t1.grid(row=0,column=2)

window.mainloop()
