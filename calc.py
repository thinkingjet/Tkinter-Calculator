# import pygame
# importing everything from tkinter library.
from tkinter import *

# Creating a TK object and calling it master.
master = Tk()


# Setting the window size
master.geometry('600x600')

# Title of GUI Window
master.title("Gaurav's Calculator")

# A placeholder, for use later, to check if the +-*/ or clear buttons are clicked. 
default = 0

# Function to check if any of the numbers are clicked
def click(no):
    x = str(no)
    nameTextField.insert(string=x,index=END)

# Functions for the plus,minus,multiply or divide.
def pl():
    global the_first_number
    the_first_number = nameTextField.get()
    nameTextField.delete(0, END)
    global default
    default = 1
def mn():
    global the_first_number
    the_first_number = nameTextField.get()
    nameTextField.delete(0, END)
    global default
    default = 2
def mul():
    global the_first_number
    the_first_number = nameTextField.get()
    nameTextField.delete(0, END)
    global default
    default = 3
def div():
    global the_first_number
    the_first_number = nameTextField.get()
    nameTextField.delete(0, END)
    global default
    default = 4

# The clear function.
def clear():
    nameTextField.delete(0, END)
    global default
    default = 0

# The text field, which shows the different characters.
nameTextField = Entry(master)

# The final function which checks gets the second number and the operator, 
# and inserts the answer in the nameTextfield.
# Equipped with error Handling, truly the best calculator in the WORLD :>)
def final():

    global the_second_number
    the_second_number = nameTextField.get()

    nameTextField.delete(0,END)
    try:
        num1 = int(the_first_number)
        num2 = int(the_second_number)

        the_sum = num1 + num2
        the_divide = num1/num2
        the_multiply = num1*num2
        the_subtract = num1-num2
    
        if default == 1:
            nameTextField.insert(string=(the_sum),index=END)
        elif default == 2:
            nameTextField.insert(string=(the_subtract),index=END)
        elif default == 3:
            nameTextField.insert(string=(the_multiply),index=END)
        elif default == 4:
            nameTextField.insert(string=(the_divide),index=END)
    except:
        nameTextField.insert(string="INVALID NUMBERS",index=END)


# All the number buttons.
b0 = Button(master,text="0", command=lambda: click(0),height=3,width=3,padx=10,pady=20)
b1 = Button(master,text="1", command=lambda: click(1),height=3,width=3,padx=10,pady=20)
b2 = Button(master,text="2", command=lambda: click(2),height=3,width=3,padx=10,pady=20)
b3 = Button(master,text="3", command=lambda: click(3),height=3,width=3,padx=10,pady=20)

b4 = Button(master,text="4", command=lambda: click(4),height=3,width=3,padx=10,pady=20)
b5 = Button(master,text="5", command=lambda: click(5),height=3,width=3,padx=10,pady=20)
b6 = Button(master,text="6", command=lambda: click(6),height=3,width=3,padx=10,pady=20)

b7 = Button(master,text="7", command=lambda: click(7),height=3,width=3,padx=10,pady=20)
b8 = Button(master,text="8", command=lambda: click(8),height=3,width=3,padx=10,pady=20)
b9 = Button(master,text="9", command=lambda: click(9),height=3,width=3,padx=10,pady=20)

# All the operators.
plus = Button(master,text="+", command=pl,height=3,width=4,padx=15,pady=15,bg="green",fg="blue")
minus = Button(master,text="-", command=mn,height=3,width=4,padx=15,pady=15,bg="green",fg="blue")
multiply = Button(master,text="X", command=mul,height=3,width=4,padx=15,pady=15,bg="green",fg="blue")
divide = Button(master,text="/", command=div,height=3,width=4,padx=15,pady=15,bg="green",fg="blue")

# The clear button
clbutton = Button(master,text="C", command=clear,height=7,width=3, padx=15,pady=10)

# The ENTER button.
equals = Button(master,text="ENTER", command=final,height=4,width=15,padx=6,pady=6)

# Plotting the different buttons.
b0.grid(row=1,column=1)
b1.grid(row=1,column=2)
b2.grid(row=1,column=3)
b3.grid(row=1,column=4)

b4.grid(row=2,column=2)
b5.grid(row=2,column=3)
b6.grid(row=2,column=4)

b7.grid(row=3,column=2)
b8.grid(row=3,column=3)
b9.grid(row=3,column=4)

# Plotting the operators.
plus.grid(row=1,column=5)
minus.grid(row=2,column=5)
multiply.grid(row=1,column=6)
divide.grid(row=2,column=6)

# PLotting The clear button.
clbutton.grid(row=2,column=1)

# Plotting the nameTextField.
nameTextField.grid(row=0,column=0,columnspan=6,padx=70,pady=30)

# Plotting the ENTER button.
equals.grid(row=3,column=5,columnspan=3)

# Prints working, confirming that everything is well so far.
print("The Calculator is Running!!!")

# The main loop which runs the calculator, and keeps on checking for input.
master.mainloop()





