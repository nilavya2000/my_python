from tkinter import*
from tkinter import messagebox
def calsum():
    fn1=int(Fno.get())
    fn2=int(Sno.get())
    r=fn1+fn2
    messagebox.showinfo("output","result="+str(r))
    messagebox.showinfo("confirmation page","done !!")
def calsub():
    fn1=int(Fno.get())
    fn2=int(Sno.get())
    r=fn1-fn2
    messagebox.showinfo("output","result="+str(r))
    messagebox.showinfo("done","result="+str(r))
    messagebox.showinfo("confirmation page","done !!")
def calmultiply():
    fn1=int(Fno.get())
    fn2=int(Sno.get())
    r=fn1*fn2
    messagebox.showinfo("output","result="+str(r))
    messagebox.showinfo("confirmation page","done !!")
def caldivide():
    fn1=int(Fno.get())
    fn2=int(Sno.get())
    r=fn1/fn2
    messagebox.showinfo("output","result="+str(r))
    messagebox.showinfo("confirmation page","done !!")
def calsqroot():
    fn1=int(Fno.get())
    fn2=int(Sno.get())
    r=fn1**(1/fn2)
    messagebox.showinfo("output","result="+str(r))
    messagebox.showinfo("confirmation page","done !!")
def calsquare():
    fn1=int(Fno.get())
    fn2=int(Sno.get())
    r=fn1**fn2
    messagebox.showinfo("output","result="+str(r))
    messagebox.showinfo("confirmation page","done !!")
###################
root=Tk()
root.title("MINI CALCULATOR")
root.geometry("600x600")
Fno=StringVar()
Sno=StringVar()
#######################
add = Button(root, text="Add",command=calsum,width=15)
subsc = Button(root, text="substract",command=calsub,width=15)
multiply = Button(root, text="multiply",command=calmultiply,width=15)
division = Button(root, text="division",command=caldivide,width=15)
cancel = Button(root,text="cancel",command=root.destroy,width=15)
sqroot = Button(root,text="sq_root",command=calsqroot,width=15)
square = Button(root,text="square",command=calsquare,width=15)
#######################
Lb11 = Label(root,text="calculation")
fst_no = Label(root,text="enter a Number")
snd_no = Label(root,text="enter  a another number")
n1 = Entry(root,width=25,textvariable=Fno)
n2 = Entry(root,width=25,textvariable=Sno)
###########################
Lb11.grid(column=1,row=1,columnspan=2)
fst_no.grid(column=1,row=2)
n1.grid(column=2,row=2)
snd_no.grid(column=1,row=3)
n2.grid(column=2,row=3)
add.grid(column=1,row=4)
subsc.grid(column=2,row=4)
multiply.grid(column=1,row=5)
division.grid(column=2,row=5)
sqroot.grid(column=1,row=6)
square.grid(column=2,row=6)
cancel.grid(column=1,row=7,columnspan=2)
############################
root.mainloop()
