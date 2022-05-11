from tkinter import *
root = Tk()
root.title("YOUR CALCULATOR")
root.geometry("510x585")
root.minsize(510,585)
root.maxsize(510,585)

root.config(bg='black')
entry = StringVar()
# root.wm_iconbitmap('1.ico')

#function
def click(event):
    global entry
    text = event.widget.cget('text')
    if text == '=':
        if entry.get().isdigit():
            value = int(entry.get())
        else:
            value = eval(entry.get())
            
        entry.set(value)
        e.update()
        
    elif text =='C':
       entry.set('')
       e.update()
    else:
        entry.set(entry.get()+text)
        e.update()

#entry widget
e = Entry(textvariable=entry,font="lucida 40 bold",bg='black',fg='yellow')
e.pack(fill=X,pady=5,padx=3)
#789
fram = Frame(root,bg='yellow',relief=SUNKEN,pady=5,background='black')
fram.pack(pady=5)
b = Button(fram,text='7',font='lucida 30 bold',bg='black',fg='yellow')
b.pack(side=LEFT,padx=10)
b.bind('<Button-1>',click)
b = Button(fram,text='8',font='lucida 30 bold',bg='black',fg='yellow')
b.pack(side=LEFT,padx=10)
b.bind('<Button-1>',click)
b = Button(fram,text='9',font='lucida 30 bold',bg='black',fg='yellow')
b.pack(side=LEFT,padx=10)
b.bind('<Button-1>',click)
b = Button(fram,text='/',font='lucida 30 bold',padx=8,bg='black',fg='yellow')
b.pack(side=LEFT,padx=10)
b.bind('<Button-1>',click)
b = Button(fram,text='C',font='lucida 30 bold',padx=8,bg='black',fg='yellow')
b.pack(side=LEFT,padx=10)
b.bind('<Button-1>',click)
#456
fram = Frame(root,bg='yellow',pady=5,background='black')
fram.pack(pady=5)
b = Button(fram,text='4',font='lucida 30 bold',bg='black',fg='yellow')
b.pack(side=LEFT,padx=10)
b.bind('<Button-1>',click)
b = Button(fram,text='5',font='lucida 30 bold',bg='black',fg='yellow')
b.pack(side=LEFT,padx=10)
b.bind('<Button-1>',click)
b = Button(fram,text='6',font='lucida 30 bold',bg='black',fg='yellow')
b.pack(side=LEFT,padx=10)
b.bind('<Button-1>',click)
b = Button(fram,text='*',font='lucida 30 bold',padx=6,bg='black',fg='yellow')
b.pack(side=LEFT,padx=10)
b.bind('<Button-1>',click)
b = Button(fram,text='%',font='lucida 30 bold',padx=4,bg='black',fg='yellow')
b.pack(side=LEFT,padx=10)
b.bind('<Button-1>',click)
# #123
fram = Frame(root,bg='yellow',pady=5,background='black')
fram.pack(pady=5)
b = Button(fram,text='1',font='lucida 30 bold',bg='black',fg='yellow')
b.pack(side=LEFT,padx=10)
b.bind('<Button-1>',click)
b = Button(fram,text='2',font='lucida 30 bold',bg='black',fg='yellow')
b.pack(side=LEFT,padx=10)
b.bind('<Button-1>',click)
b = Button(fram,text='3',font='lucida 30 bold',bg='black',fg='yellow')
b.pack(side=LEFT,padx=10)
b.bind('<Button-1>',click)
b = Button(fram,text='-',font='lucida 30 bold',padx=7,bg='black',fg='yellow')
b.pack(side=LEFT,padx=10)
b.bind('<Button-1>',click)
b = Button(fram,text='+',font='lucida 30 bold',padx=10,bg='black',fg='yellow')
b.pack(side=LEFT,padx=10)
b.bind('<Button-1>',click)
#= .  0
fram = Frame(root,bg='yellow',pady=5,background='black')
fram.pack(pady=5)
b = Button(fram,text='0',font='lucida 30 bold',bg='black',fg='yellow')
b.pack(side=LEFT,padx=10)
b.bind('<Button-1>',click)
b = Button(fram,text='.',font='lucida 30 bold',padx=7.35,bg='black',fg='yellow')
b.pack(side=LEFT,padx=10)
b.bind('<Button-1>',click)

b.bind('<Button-1>',click)
b = Button(fram,text='=',font='lucida 30 bold',padx=110,bg='black',fg='yellow')
b.pack(side=LEFT,padx=10)
b.bind('<Button-1>',click)
root.mainloop()