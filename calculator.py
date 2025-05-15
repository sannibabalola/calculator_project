from tkinter import *

window = Tk()
window.title('simple calculator')  # Title of the project
window.geometry("300x200")
window.resizable(False, False)
window.config(bg="#1e1e2f")


# Create input box widget (entry)
e = Entry(window, font=("Arial", 11), width=35, bg="#000", fg="#0f0")
# Displaying the input box widget (entry)
e.grid(row=0, column=0, columnspan=4, padx=5, pady=5, ipady=10)
# Set the initial value on screen to zero
e.insert(0, 0)


# Define function for each number buttton
def button_click(number):
    current = e.get()
   # Remove the first zero only if it is the leading zero
    if current == "0":
        current = ""
    e.delete(0, END)
    e.insert(0, current + str(number))

# Define function for clear button


def button_clear():
    e.delete(0, END)
    e.insert(0, 0)


# Define function for add button
def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

# Define function for "subtraction" button


def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

# Define function for "multiplication" button


def button_mul():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

# Define function for "division" button


def button_div():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

# Define function for equal button


def button_equal():
    # Performs addition if + sign click
    if math == "addition":
        second_number = e.get()
        e.delete(0, END)
        e.insert(0, f_num + int(second_number))

    # Performs "subtraction" if - sign click
    elif math == "subtraction":
        second_number = e.get()
        e.delete(0, END)
        e.insert(0, f_num - int(second_number))

    # Performs "multiplication" if * sign click
    elif math == "multiplication":
        second_number = e.get()
        e.delete(0, END)
        e.insert(0, f_num * int(second_number))

    # Performs "division" if / sign click
    elif math == "division":
        second_number = e.get()
        e.delete(0, END)
        try:
            e.insert(0, f_num / int(second_number))
        except ZeroDivisionError:
            e.insert(0, "Error")


# Creating the buttons
button_1 = Button(window, text="1", width=6, padx=10,
                  pady=5, command=lambda: button_click(1))
button_2 = Button(window, text="2", width=6, padx=10,
                  pady=5, command=lambda: button_click(2))
button_3 = Button(window, text="3", width=6, padx=10,
                  pady=5, command=lambda: button_click(3))
button_4 = Button(window, text="4", width=6, padx=10,
                  pady=5, command=lambda: button_click(4))
button_5 = Button(window, text="5", width=6, padx=10,
                  pady=5, command=lambda: button_click(5))
button_6 = Button(window, text="6", width=6, padx=10,
                  pady=5, command=lambda: button_click(6))
button_7 = Button(window, text="7", width=6, padx=10,
                  pady=5, command=lambda: button_click(7))
button_8 = Button(window, text="8", width=6, padx=10,
                  pady=5, command=lambda: button_click(8))
button_9 = Button(window, text="9", width=6, padx=10,
                  pady=5, command=lambda: button_click(9))
button_0 = Button(window, text="0", width=6, padx=10,
                  pady=5, command=lambda: button_click(0))
button_add = Button(window, text="+", width=6, padx=10,
                    pady=5, command=button_add)
button_sub = Button(window, text="-", width=6, padx=10,
                    pady=5, command=button_sub)
button_mul = Button(window, text="*", width=6, padx=10,
                    pady=5, command=button_mul)
button_div = Button(window, text="/", width=6, padx=10,
                    pady=5, command=button_div)
button_equal = Button(window, text="=", width=6, padx=10, pady=5,
                      command=button_equal)
button_clear = Button(window, text="C", width=6, bg='red', fg='white', padx=10, pady=5,
                      command=button_clear)
# Display the button
button_1.grid(row=3, column=0, )
button_2.grid(row=3, column=1, )
button_3.grid(row=3, column=2, )
button_4.grid(row=2, column=0, )
button_5.grid(row=2, column=1, )
button_6.grid(row=2, column=2, )
button_7.grid(row=1, column=0, )
button_8.grid(row=1, column=1, )
button_9.grid(row=1, column=2, )
button_0.grid(row=4, column=0, )
button_add.grid(row=4, column=3, )
button_sub.grid(row=3, column=3, )
button_mul.grid(row=2, column=3, )
button_div.grid(row=1, column=3, )
button_equal.grid(row=4, column=1, )
button_clear.grid(row=4, column=2, )


window.mainloop()
