from tkinter import *

app = Tk()
app.title("CalcPy")


user_input = Entry(app, width =30)
user_input.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Operation Functions
def numeric_button():
    print("you pressed a numeric button")


def addition():
    print("youre trying to add ")


def subtraction():
    print("youre trying to subtract")


def multiplication():
    print("youre trying to multiply")


def division():
    print("youre trying to divide..are you america?")


def clear():
    print("youre trying to clear")


# Numeric Buttons
button_0 = Button(app, text=" 0 ", padx=40, pady=20, command=numeric_button).grid(row=4, column=1)
button_1 = Button(app, text=" 1 ", padx=40, pady=20, command=numeric_button).grid(row=3, column=0)
button_2 = Button(app, text=" 2 ", padx=40, pady=20, command=numeric_button).grid(row=3, column=1)
button_3 = Button(app, text=" 3 ", padx=40, pady=20, command=numeric_button).grid(row=3, column=2)
button_4 = Button(app, text=" 4 ", padx=40, pady=20, command=numeric_button).grid(row=2, column=0)
button_5 = Button(app, text=" 5 ", padx=40, pady=20, command=numeric_button).grid(row=2, column=1)
button_6 = Button(app, text=" 6 ", padx=40, pady=20, command=numeric_button).grid(row=2, column=2)
button_7 = Button(app, text=" 7 ", padx=40, pady=20, command=numeric_button).grid(row=1, column=0)
button_8 = Button(app, text=" 8 ", padx=40, pady=20, command=numeric_button).grid(row=1, column=1)
button_9 = Button(app, text=" 9 ", padx=40, pady=20, command=numeric_button).grid(row=1, column=2)

# Operation Buttons
button_add = Button(app, text=" + ", command=addition, padx=43, pady=23).grid(row=1, column=3, columnspan=1)
button_subtract = Button(app, text=" - ", command=subtraction, padx=43, pady=23).grid(row=2, column=3, columnspan=1)
button_divide = Button(app, text=" / ", command=division, padx=43, pady=23).grid(row=3, column=3, columnspan=1)
button_multiply = Button(app, text=" * ", command=multiplication, padx=43, pady=23).grid(row=4, column=3, columnspan=1)
button_equals = Button(app, text=" = ", command=numeric_button, padx=43, pady=23).grid(row=4, column=2)
button_clear = Button(app, text=" CLEAR ", command=clear, padx=43, pady=23).grid(row=4, column=0)


app.mainloop()