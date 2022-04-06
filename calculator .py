from tkinter import *
win=Tk()
win.title("Calculator by Hamzafayaz")
# win.wm_iconbitmap("512.png")
def click(envent):
     text1=envent.widget.cget("text")
     if text1=="=":
         if output.get().isdigit():
             value=int(output.get())
         else:
             try:
                 value=(eval(output.get()))
             except Exception as e:
                 value="ERROR"
         output.set(value)
         screen.update()

     elif text1=="C":
         output.set("")
     else:
        output.set(output.get()+text1)
        screen.update()

win.geometry("400x700")
win.maxsize(400,700)
win.minsize(400,700)
output=StringVar()
screen=Entry(win,textvariable=output,font="lucida 20 bold",bd=5)
screen.pack(fill=X)
f=Frame(win,bg="skyblue")
f.pack()
list1=['9','8','7']
for i in list1:
    b=Button(f,text=i,font="lucida 20 bold",padx=15,pady=15)
    b.pack(side=LEFT,pady=10,padx=5)
    b.bind('<Button-1>',click)
f=Frame(win,bg="skyblue")
f.pack()
list2=['6','5','4']
for i in list2:
    b=Button(f,text=i,font="lucida 20 bold",padx=15,pady=15)
    b.pack(side=LEFT,pady=10,padx=5)
    b.bind('<Button-1>',click)
f=Frame(win,bg="skyblue")
f.pack()
list2=['3','2','1']
for i in list2:
    b=Button(f,text=i,font="lucida 20 bold",padx=15,pady=15)
    b.pack(side=LEFT,pady=10,padx=5)
    b.bind('<Button-1>',click)
f=Frame(win,bg="skyblue")
f.pack()
list2=['0','+','-']
for i in list2:
    b=Button(f,text=i,font="lucida 20 bold",padx=15,pady=15)
    b.pack(side=LEFT,pady=10,padx=6)
    b.bind('<Button-1>',click)
f=Frame(win,bg="skyblue")
f.pack()
list2=['.','/','=']
for i in list2:
    b=Button(f,text=i,font="lucida 20 bold",padx=15,pady=15)
    b.pack(side=LEFT,pady=10,padx=6.7)
    b.bind('<Button-1>',click)
f=Frame(win,bg="skyblue")
f.pack()
list2=['*','C','%']
for i in list2:
    b=Button(f,text=i,font="lucida 20 bold",padx=15,pady=15)
    b.pack(side=LEFT,pady=10,padx=3.4)
    b.bind('<Button-1>',click)
win.mainloop()