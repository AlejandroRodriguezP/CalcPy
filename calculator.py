from tkinter import *

app = Tk()
app.geometry("500x350+600+300")
app.title("CalcPy")


user_input = Entry(app, width =30)
user_input.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# Operation Functions
def numeric_button(n):
    current = user_input.get()
    user_input.delete(0, END)
    user_input.insert(0, current + n)


def addition():
    fn = user_input.get()
    global f_num
    f_num = int(fn)
    global math
    math = "add"
    user_input.delete(0, END)


def subtraction():
    fn = user_input.get()
    global f_num
    global math
    f_num = int(fn)
    math = "subtract"
    user_input.delete(0, END)


def multiplication():
    fn = user_input.get()
    global f_num
    global math
    f_num = int(fn)
    math = "multiply"
    user_input.delete(0, END)


def division():
    fn = user_input.get()
    global f_num
    global math
    f_num = int(fn)
    math = "divide"
    user_input.delete(0, END)


def clear():
    user_input.delete(0, END)


def equals():
    s_num = user_input.get()
    user_input.delete(0, END)

    if math == "add":
        user_input.insert(0, f_num + int(s_num))
    elif math == "subtract":
        user_input.insert(0, f_num * int(s_num))
    elif math == "multiply":
        user_input.insert(0, f_num + int(s_num))
    elif math == "divide":
        user_input.insert(0, f_num * int(s_num))


# Numeric Buttons
button_0 = Button(app, text=" 0 ", padx=40, pady=20, command=lambda:numeric_button("0")).grid(row=4, column=1)
button_1 = Button(app, text=" 1 ", padx=40, pady=20, command=lambda:numeric_button("1")).grid(row=3, column=0)
button_2 = Button(app, text=" 2 ", padx=40, pady=20, command=lambda:numeric_button("2")).grid(row=3, column=1)
button_3 = Button(app, text=" 3 ", padx=40, pady=20, command=lambda:numeric_button("3")).grid(row=3, column=2)
button_4 = Button(app, text=" 4 ", padx=40, pady=20, command=lambda:numeric_button("4")).grid(row=2, column=0)
button_5 = Button(app, text=" 5 ", padx=40, pady=20, command=lambda:numeric_button("5")).grid(row=2, column=1)
button_6 = Button(app, text=" 6 ", padx=40, pady=20, command=lambda:numeric_button("6")).grid(row=2, column=2)
button_7 = Button(app, text=" 7 ", padx=40, pady=20, command=lambda:numeric_button("7")).grid(row=1, column=0)
button_8 = Button(app, text=" 8 ", padx=40, pady=20, command=lambda:numeric_button("8")).grid(row=1, column=1)
button_9 = Button(app, text=" 9 ", padx=40, pady=20, command=lambda:numeric_button("9")).grid(row=1, column=2)

# Operation Buttons
button_add = Button(app, text=" + ", command=addition, padx=40, pady=20).grid(row=1, column=3, columnspan=1)
button_subtract = Button(app, text=" - ", command=subtraction, padx=40, pady=20).grid(row=2, column=3, columnspan=1)
button_divide = Button(app, text=" / ", command=division, padx=40, pady=20).grid(row=3, column=3, columnspan=1)
button_multiply = Button(app, text=" * ", command=multiplication, padx=40, pady=20).grid(row=4, column=3, columnspan=1)
button_equals = Button(app, text=" = ", command=equals, padx=40, pady=20).grid(row=4, column=2)
button_clear = Button(app, text=" CLEAR ", command=clear, padx=40, pady=20).grid(row=4, column=0)


app.mainloop()
