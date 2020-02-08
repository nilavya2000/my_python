from tkinter import *
from tkinter import messagebox
import goslate
import b


def fr():
    d=v.get()
    b=a.translate(d,'fr')
    messagebox.showinfo("translated","french = {}".format(b))

def sp():
    d=v.get()
    b=a.translate(d,'es')
    messagebox.showinfo("translated","spanish = {}".format(b))

def bn():
    d=v.get()
    b=a.translate(d,'bn')
    messagebox.showinfo("translated","bengali = {}".format(b))

def view_command():
    list1.delete(0,END)
    for row in b.view():
        list1.insert(END,row)


root=Tk()
root.title("Translator")
a=goslate.Goslate()
v=StringVar()

t=Label(root, text='TRANSLATOR')
t.grid(row=1, column=1, columnspan=3)

b1=Button(root, text='FRENCH', command=fr)
b1.grid(row=3, column=1)

b2=Button(root, text='SPANISH',command=sp)
b2.grid(row=3, column=2)

b3=Button(root, text='BENGALI',command=bn)
b3.grid(row=3, column=3)

b4=Button(root, text='CANCEL',command=root.destroy)
b4.grid(row=5, column=1)

b5=Button(root, text='HISTORY')
b5.grid(row=5, column=2)

l=Label(root, text='Enter the word')
l.grid(row=2, column=1)

e=Entry(root, width=25, textvariable=v)
e.grid(row=2,column=2,columnspan=2)

list1=Listbox(root, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

root.mainloop()
