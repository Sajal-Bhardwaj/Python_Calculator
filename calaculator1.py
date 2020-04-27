from tkinter import *
from math import *

cal=Tk()
cal.configure(bg='black')
cal.title("Calculator",)
enter=Entry(cal,width=28,borderwidth=5,font=("Times New Roman",24),justify='right')
enter.grid(row=0,column=0,columnspan=5)

def click(number):
    enter.insert(END,number)

def clear():
    enter.delete(0,END)

def sin_func():
    global first_number
    global function
    first_number=enter.get()
    enter.delete(0,END)
    enter.insert(0,sin(pi/float(first_number)))

def cos_func():
    global first_number
    global function
    first_number=enter.get()
    enter.delete(0,END)
    enter.insert(0,cos(pi/float(first_number)))

def tan_func():
    global first_number
    global function
    first_number=enter.get()
    enter.delete(0,END)
    enter.insert(0,tan(pi/float(first_number)))

def fcatorial_func():
    global first_number
    global function
    fact=1
    first_number=enter.get()
    enter.delete(0,END)
    if first_number==0:
        enter.insert(0,fact)
    else:
        for i in range (1,int(first_number)+1):
            fact = fact * i
        enter.insert(0,fact)

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

def cube_root():
    global first_number
    global function
    first_number=enter.get()
    enter.delete(0,END)
    enter.insert(0,round(float(first_number)**(1/3)))

def fourth_root():
    global first_number
    global function
    first_number=enter.get()
    enter.delete(0,END)
    enter.insert(0,round(float(first_number)**(1/4)))

def half():
    global first_number
    global function
    first_number=enter.get()
    enter.delete(0,END)
    enter.insert(0,float(first_number)/2)


def Ln_function():
    global first_number
    global function
    first_number=enter.get()
    enter.delete(0,END)
    enter.insert(0,log(float(first_number)))


def Log_func():

    global first_number
    global function
    first_number=enter.get()
    enter.delete(0,END)
    enter.insert(0,log10(float(first_number)))

def Convert_to_Faranheit():

    global first_number
    global function
    first_number=enter.get()
    enter.delete(0,END)
    enter.insert(0,float(first_number)*1.8+32)


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

button10=Button(cal,text="0",padx=30,pady=20,bg="black",fg="white",font=("Times New Roman",18),command=lambda :click(0))
button11=Button(cal,text="%",padx=25,pady=20,bg="#464648",fg="white",font=("Times New Roman",18),command=mod)
button12=Button(cal,text="^",padx=31,pady=20,bg="#464648",fg="white",font=("Times New Roman",18),command=power)
button13=Button(cal,text="√",padx=30,pady=20,bg="#464648",fg="white",font=("Times New Roman",18),command=square_root)
button14=Button(cal,text="1/x",padx=20,pady=20,bg="#464648",fg="white",font=("Times New Roman",18),command=half)
button_equal=Button(cal,text="=",padx=30,pady=20,bg="#464648",fg="white",font=("Times New Roman",18),command=equals_to)
button_Add=Button(cal,text="+",padx=28,pady=20,bg='#464648',fg="white",font=("Times New Roman",18),command=add)
button_Sub=Button(cal,text="-",padx=30,pady=20,bg='#464648',fg="white",font=("Times New Roman",18),command=sub)
button_Mult=Button(cal,text="X",padx=25,pady=20,bg='#464648',fg="white",font=("Times New Roman",18),command=mult)
button_Devide=Button(cal,text="/",padx=31,pady=20,bg='#464648',fg="white",font=("Times New Roman",18),command=dev)
button_Clear=Button(cal,text="C",padx=29,pady=20,bg="#464648",fg="white",font=("Times New Roman",18),command=clear)

button_Sin=Button(cal,text="Sin",padx=21,pady=18,bg="#464648",fg="white",font=("Times New Roman",18),command=sin_func)
button_Cosin=Button(cal,text="Cos",padx=17,pady=18,bg="#464648",fg="white",font=("Times New Roman",18),command=cos_func)
button_Tan=Button(cal,text="Tan",padx=17,pady=18,bg="#464648",fg="white",font=("Times New Roman",18),command=tan_func)
button_Log=Button(cal,text="log",padx=20,pady=18,bg="#464648",fg="white",font=("Times New Roman",18),command=Log_func)
button_Ln=Button(cal,text="ln",padx=27,pady=18,bg="#464648",fg="white",font=("Times New Roman",18),command=Ln_function)
button_CubeRoot=Button(cal,text="∛",padx=27,pady=20,bg="#464648",fg="white",font=("Times New Roman",18),command=cube_root)
button_Fourth_Root=Button(cal,text="∜",padx=27,pady=20,bg="#464648",fg="white",font=("Times New Roman",18),command=fourth_root)
button_Factorial=Button(cal,text="!",padx=32,pady=20,bg="#464648",fg="white",font=("Times New Roman",18),command=fcatorial_func)
button_Pi=Button(cal,text="π",padx=30,pady=20,bg="#464648",fg="white",font=("Times New Roman",18),command=lambda:click(pi))
button_Faranheit_C=Button(cal,text="C->F",padx=8,pady=20,bg="#464648",fg="white",font=("Times New Roman",18),command=Convert_to_Faranheit)


button1.grid(row=5,column=0)
button2.grid(row=5,column=1)
button3.grid(row=5,column=2)

button4.grid(row=4,column=0)
button5.grid(row=4,column=1)
button6.grid(row=4,column=2)

button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)

button10.grid(row=6,column=1)
button11.grid(row=6,column=3)
button12.grid(row=2,column=0)
button13.grid(row=2,column=4)
button14.grid(row=2,column=2)

button_Devide.grid(row=2,column=3)
button_Mult.grid(row=3,column=3)
button_Sub.grid(row=4,column=3)
button_Add.grid(row=5,column=3)
button_equal.grid(row=6,column=4)
button_Clear.grid(row=6,column=0)

button_Sin.grid(row=1,column=0)
button_Cosin.grid(row=1,column=1)
button_Tan.grid(row=1,column=2)
button_Log.grid(row=1,column=3)
button_Ln.grid(row=1,column=4)
button_CubeRoot.grid(row=3,column=4)
button_Fourth_Root.grid(row=4,column=4)
button_Factorial.grid(row=5,column=4)
button_Pi.grid(row=2,column=1)
button_Faranheit_C.grid(row=6,column=2)



enter.mainloop()
