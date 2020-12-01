from tkinter import *
import pyglet, os
root = Tk()

e = Entry(root, width=20, borderwidth=1, bg="olive", fg="white")
e.grid(row=0, column=0, columnspan=6, padx=75, pady=1)
e.configure(font=("Digital-7 Mono", 20, "bold"))

def button_click(number):
    current=e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def clear(number):
    e.delete(0,END)

def add():
    first =e.get()
    global f_num
    f_num=int(first)
    e.delete(0, END)

def equals():
    ayt=e.get()
    global dd
    dd=int(ayt)
    e.delete(0, END)
    if myButtonplus:
        e.insert(0, int(ayt) + (int(f_num)))


myButton9 = Button(root, text = "9", padx=40, pady=20, fg="white", bg="black",command=lambda:button_click(9))
myButton8 = Button(root, text = "8",  padx=40, pady=20,fg="white", bg="black", command=lambda:button_click(8))
myButton7 = Button(root, text = "7",  padx=40, pady=20,fg="white", bg="black", command=lambda:button_click(7))
myButton6 = Button(root, text = "6",  padx=40, pady=20,fg="white", bg="black", command=lambda:button_click(6))
myButton5 = Button(root, text = "5",  padx=40, pady=20,fg="white", bg="black", command=lambda:button_click(5))
myButton4 = Button(root, text = "4",  padx=40, pady=20,fg="white", bg="black",  command=lambda:button_click(6))
myButton3 = Button(root, text = "3",  padx=40, pady=20,fg="white", bg="black",  command=lambda:button_click(7))
myButton2 = Button(root, text = "2",  padx=40, pady=20,fg="white", bg="black", command=lambda:button_click(2))
myButton1 = Button(root, text = "1",  padx=40, pady=20,fg="white", bg="black", command=lambda:button_click(1))
myButton0 = Button(root, text = "0",  padx=40, pady=20,fg="white", bg="black", command=lambda:button_click(0))
myButtonequals = Button(root, text = "=",  padx=40, pady=20,fg="white", bg="black", command=equals)
myButtonplus = Button(root, text = "+",  padx=40, pady=20,fg="white", bg="black", command=add)
myButtonclear = Button(root, text = "AC", padx=35, pady=20,fg="white", bg="black", command=lambda:clear(0))


myButton9.grid(row=1, column=2)
myButton7.grid(row=1, column=0)
myButton8.grid(row=1, column=1)

myButton5.grid(row=2, column=1)
myButton4.grid(row=2, column=0)
myButton3.grid(row=3, column=2)

myButton2.grid(row=3, column=1)
myButton1.grid(row=3, column=0)
myButton0.grid(row=4, column=0)

myButton6.grid(row=2, column=2)
myButtonplus.grid(row=1, column=5)
myButtonequals.grid(row=2, column=5)
myButtonclear.grid(row=4, column=5)

myButton0.configure(font=("Digital-7 Mono", 20))
myButton1.configure(font=("Digital-7 Mono", 20))
myButton2.configure(font=("Digital-7 Mono", 20))
myButton3.configure(font=("Digital-7 Mono", 20))
myButton4.configure(font=("Digital-7 Mono", 20))
myButton5.configure(font=("Digital-7 Mono", 20))
myButton6.configure(font=("Digital-7 Mono", 20))
myButton7.configure(font=("Digital-7 Mono", 20))
myButton8.configure(font=("Digital-7 Mono", 20))
myButton9.configure(font=("Digital-7 Mono", 20))
myButtonplus.configure(font=("Digital-7 Mono", 20))
myButtonequals.configure(font=("Digital-7 Mono", 20))
myButtonclear.configure(font=("Digital-7 Mono", 20))


root.configure(background='black')
root.title("Calculator")
root.mainloop()
