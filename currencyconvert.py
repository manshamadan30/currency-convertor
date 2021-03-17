from tkinter import *
window = Tk()

def conversionInr():
    indian=(float(dollars.get())*75)
    t1.delete("1.0",END)
    t1.insert(END,indian)

def conversioncanada():
    canada=(float(dollars.get())*1.3)
    t2.delete("1.0",END)
    t2.insert(END,canada)


def conversioneuro():
    euro=(float(dollars.get())*0.84)
    t3.delete("1.0",END)
    t3.insert(END,euro)





b1=Button(window, text="Conert into INR", command=conversionInr)
b1.grid(row=2,column=0)

b2=Button(window, text="Conert into Canadian dollar", command=conversioncanada)
b2.grid(row=2,column=1)

b3=Button(window, text="Conert into Euro", command=conversioneuro)
b3.grid(row=2,column=2)


dollars=StringVar()
e1=Entry(window,textvariable=dollars)
e1.grid(row=0,column=1)

t1=Text(window ,height=2,width=10)
t1.grid(row=1,column=0)

t2=Text(window ,height=2,width=10)
t2.grid(row=1,column=1)

t3=Text(window ,height=2,width=10)
t3.grid(row=1,column=2)

window.mainloop()