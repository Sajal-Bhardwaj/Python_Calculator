from tkinter import *
import math

cal=Tk()
cal.configure(bg='black')
cal.title("Calculator",)
enter=Entry(cal,width=30,borderwidth=5,font=("Times New Roman",18),justify='right')
enter.grid(row=0,column=0,columnspan=4)

def click(number):
    enter.insert(END,number)

def clear():
    enter.delete(0,END)

def add():

    global first_number
    global function
    first_number=enter.get()
    enter.delete(0,END)
    function="+"
def sub():
    global first_number
    global function
    first_number=enter.get()
    enter.delete(0,END)
    function="-"
def mult():
    global first_number
    global function
    first_number=enter.get()
    enter.delete(0,END)
    function="*"
def dev():
    global first_number
    global function
    first_number=enter.get()
    enter.delete(0,END)
    function="/"
def mod():
    global first_number
    global function
    first_number=enter.get()
    enter.delete(0,END)
    function="%"
def power():
    global first_number
    global function
    first_number=enter.get()
    enter.delete(0,END)
    function="^"

def square_root():
    global first_number
    global function
    first_number=enter.get()
    enter.delete(0,END)
    enter.insert(0,math.sqrt(float(first_number)))

def half():
    global first_number
    global function
    first_number=enter.get()
    enter.delete(0,END)
    enter.insert(0,float(first_number)/2)




def equals_to():
    sec_num=enter.get()
    enter.delete(0,END)
    if function=="+":
        enter.insert(0,float(first_number)+ float(sec_num))
    if function=="-":
        enter.insert(0,float(first_number)- float(sec_num))
    if function=="*":
        enter.insert(0,float(first_number)* float(sec_num))
    if function=="/":
        enter.insert(0,float(first_number)/ float(sec_num))
    if function=="%":
        enter.insert(0,float(first_number)% float(sec_num))
    if function=="^":
        enter.insert(0,float(first_number)**float(sec_num))

#Deffine buttons
button1=Button(cal,text="1",padx=30,pady=20,bg="black",fg="white",font=("Times New Roman",18),command=lambda :click(1))
button2=Button(cal,text="2",padx=30,pady=20,bg="black",fg="white",font=("Times New Roman",18),command=lambda :click(2))
button3=Button(cal,text="3",padx=30,pady=20,bg="black",fg="white",font=("Times New Roman",18),command=lambda :click(3))

button4=Button(cal,text="4",padx=30,pady=20,bg="black",fg="white",font=("Times New Roman",18),command=lambda :click(4))
button5=Button(cal,text="5",padx=30,pady=20,bg="black",fg="white",font=("Times New Roman",18),command=lambda :click(5))
button6=Button(cal,text="6",padx=31,pady=20,bg="black",fg="white",font=("Times New Roman",18),command=lambda :click(6))

button7=Button(cal,text="7",padx=30,pady=20,bg="black",fg="white",font=("Times New Roman",18),command=lambda :click(7))
button8=Button(cal,text="8",padx=30,pady=20,bg="black",fg="white",font=("Times New Roman",18),command=lambda :click(8))
button9=Button(cal,text="9",padx=30,pady=20,bg="black",fg="white",font=("Times New Roman",18),command=lambda :click(9))

button10=Button(cal,text="0",padx=32,pady=20,bg="black",fg="white",font=("Times New Roman",18),command=lambda :click(0))
button11=Button(cal,text="%",padx=27,pady=20,bg="#464648",fg="white",font=("Times New Roman",18),command=mod)
button12=Button(cal,text="^",padx=31,pady=20,bg="#464648",fg="white",font=("Times New Roman",18),command=power)
button13=Button(cal,text="√",padx=30,pady=20,bg="#464648",fg="white",font=("Times New Roman",18),command=square_root)
button14=Button(cal,text="1/x",padx=20,pady=20,bg="#464648",fg="white",font=("Times New Roman",18),command=half)

button_equal=Button(cal,text="=",padx=30,pady=20,bg="#464648",fg="white",font=("Times New Roman",18),command=equals_to)
button_Add=Button(cal,text="+",padx=30,pady=20,bg='#464648',fg="white",font=("Times New Roman",18),command=add)
button_Sub=Button(cal,text="-",padx=32,pady=20,bg='#464648',fg="white",font=("Times New Roman",18),command=sub)
button_Mult=Button(cal,text="X",padx=28,pady=20,bg='#464648',fg="white",font=("Times New Roman",18),command=mult)
button_Devide=Button(cal,text="/",padx=32,pady=20,bg='#464648',fg="white",font=("Times New Roman",18),command=dev)
button_clear=Button(cal,text="C",padx=29,pady=20,bg="#464648",fg="white",font=("Times New Roman",18),command=clear)

button1.grid(row=4,column=0)
button2.grid(row=4,column=1)
button3.grid(row=4,column=2)

button4.grid(row=3,column=0)
button5.grid(row=3,column=1)
button6.grid(row=3,column=2)

button7.grid(row=2,column=0)
button8.grid(row=2,column=1)
button9.grid(row=2,column=2)

button10.grid(row=5,column=1)
button11.grid(row=5,column=2)
button12.grid(row=1,column=0)
button13.grid(row=1,column=1)
button14.grid(row=1,column=2)

button_Devide.grid(row=1,column=3)
button_Mult.grid(row=2,column=3)
button_Sub.grid(row=3,column=3)
button_Add.grid(row=4,column=3)
button_equal.grid(row=5,column=3)
button_clear.grid(row=5,column=0)



enter.mainloop()
