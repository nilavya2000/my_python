from tkinter import *
from tkinter import messagebox
import json
from difflib import get_close_matches

window=Tk()
window.title("dictionary")
word=StringVar()
y=StringVar()



def a():
    w=word.get()
    w=w.lower()
    data=json.load(open("data.json"))
    if w in data:
        messagebox.showinfo("result","search = "+data[w])

    elif w.title() in data:
        messagebox.showinfo("result","search = "+data[w.title()])

    elif w.upper() in data:
        messagebox.showinfo("result","search = "+data[w.upper()])

    #elif len(get_close_matches(w, data.keys())) >0:
    #    yn=input("did you mean %s instead ? enter Y if yes or N if no : "%get_close_matches(w, data.keys())[0])
    #    yn=yn.lower()
    #    if yn=='y':
    #        messagebox.showinfo("result","search = "+StringVar(data[get_close_matches(w, data.keys())[0]])
    #    elif yn=='n':
    #        messagebox.showinfo("result","the word doesn't exist. plz do double check it")
    #    else:
    #        messagebox.showinfo("result","we can't get you.")

search=Button(window,text='search',command=a)
search.grid(row=3, column=2)

word=dict()
word=Entry(window,textvariable=word)
word.grid(row=2,column=2)




window.mainloop()
