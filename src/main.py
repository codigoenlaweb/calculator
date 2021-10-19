from tkinter import *
from tkinter import font
from typing import Sized

root = Tk()
root.title("calculator")

#   VARIABLES
i = 0

#   FUNCTION
#   ADD INPUT
def click_button(e):
    global i
    e_text.insert(i, e)
    i += 1
#   REMOVE INPUT
def clean():
    global i
    e_text.delete(0, END)
    i = 0

def result():
    global i
    equation = e_text.get()
    equation_filter_x = equation.replace("x", "*")
    equation_filter_exp = equation_filter_x.replace("^", "**")
    equation_result = eval(equation_filter_exp)
    e_text.delete(0, END)
    e_text.insert(i, equation_result)
    i = 0



#   INPUT
e_text = Entry(root)


# BUTTON
#   NUMBER
btn1 = Button(root, command= lambda: click_button(1))
btn2 = Button(root, command= lambda: click_button(2))
btn3 = Button(root, command= lambda: click_button(3))
btn4 = Button(root, command= lambda: click_button(4))
btn5 = Button(root, command= lambda: click_button(5))
btn6 = Button(root, command= lambda: click_button(6))
btn7 = Button(root, command= lambda: click_button(7))
btn8 = Button(root, command= lambda: click_button(8))
btn9 = Button(root, command= lambda: click_button(9))
btn0 = Button(root, command= lambda: click_button(0))
#   ACTION
btn_delete = Button(root, command= lambda: clean())
btn_barckets_left = Button(root, command= lambda: click_button("("))
btn_barckets_right = Button(root, command= lambda: click_button(")"))
btn_decimal = Button(root, command= lambda: click_button("."))
btn_equal = Button(root, command= lambda: result())
#   OPERATOR
btn_sum = Button(root, command= lambda: click_button("+"))
btn_subt = Button(root, command= lambda: click_button("-"))
btn_mult = Button(root, command= lambda: click_button("x"))
btn_division = Button(root, command= lambda: click_button("/"))
btn_exp = Button(root, command= lambda: click_button("^"))


#   CONFIG STYLE
#   INPUT
e_text.config(font=("calibri 20"), width=14)
#   NUMBER
btn1.config(text="1", width=5, height=2)
btn2.config(text="2", width=5, height=2)
btn3.config(text="3", width=5, height=2)
btn4.config(text="4", width=5, height=2)
btn5.config(text="5", width=5, height=2)
btn6.config(text="6", width=5, height=2)
btn7.config(text="7", width=5, height=2)
btn8.config(text="8", width=5, height=2)
btn9.config(text="9", width=5, height=2)
btn0.config(text="0", width=5, height=2)
#   ACTION
btn_delete.config(text="AC", width=5, height=2)
btn_barckets_left.config(text="(", width=5, height=2)
btn_barckets_right.config(text=")", width=5, height=2)
btn_decimal.config(text=".", width=5, height=2)
btn_equal.config(text="=", width=5, height=2)
#   OPERATOR
btn_sum.config(text="+", width=5, height=2)
btn_subt.config(text="-", width=5, height=2)
btn_mult.config(text="x", width=5, height=2)
btn_division.config(text="÷", width=5, height=2)
btn_exp.config(text="exp", width=5, height=2)


#   GRID
#   INPUT
e_text.grid(row=0, column=0, columnspan=4, padx=10, pady=5)
#   NUMBER
btn1.grid(row=4, column=0, padx=0, pady=6)
btn2.grid(row=4, column=1, padx=0, pady=6)
btn3.grid(row=4, column=2, padx=0, pady=6)
btn4.grid(row=3, column=0, padx=0, pady=6)
btn5.grid(row=3, column=1, padx=0, pady=6)
btn6.grid(row=3, column=2, padx=0, pady=6)
btn7.grid(row=2, column=0, padx=0, pady=6)
btn8.grid(row=2, column=1, padx=0, pady=6)
btn9.grid(row=2, column=2, padx=0, pady=6)
btn0.grid(row=5, column=1, padx=0, pady=6)
#   ACTION
btn_delete.grid(row=1, column=0, padx=0, pady=6)
btn_barckets_left.grid(row=1, column=1, padx=0, pady=6)
btn_barckets_right.grid(row=1, column=2, padx=0, pady=6)
btn_decimal.grid(row=5, column=0, padx=0, pady=6)
btn_equal.grid(row=5, column=3, padx=0, pady=6)
#   OPERATOR
btn_sum.grid(row=3, column=3, padx=0, pady=6)
btn_subt.grid(row=4, column=3, padx=0, pady=6)
btn_mult.grid(row=2, column=3, padx=0, pady=6)
btn_division.grid(row=1, column=3, padx=0, pady=6)
btn_exp.grid(row=5, column=2, padx=0, pady=6)

root.mainloop()
