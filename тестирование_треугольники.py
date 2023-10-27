from tkinter import*
import re

def check_triangle():
    x = int(entry1.get())
    y = int(entry2.get())
    z = int(entry3.get())

    if x + y <= z or (x == 0 and y == 0 and z == 0) or (x == 1 and y == 1 and z == 1):
        result_label.config(text="Треугольника с данными значениями не существует, попробуйте другие значения.")
    elif x > 1 and y > 1 and z > 1 and x == y and y == z and x + y > z:
        result_label.config(text="Данный треугольник - равносторонний.")
    elif x > 1 and y > 1 and z > 1 and x + y > z:
        result_label.config(text="Данный треугольник - разносторонний.")
    elif (x > 1 and y > 1 and z > 1) and (x == y and x != z or x == z and x != y or y == z and y != x):
        result_label.config(text="Данный треугольник - равнобедренный.")
    else:
        result_label.config(text="Треугольника с данными значениями не существует, попробуйте другие значения.")


window = Tk()
window.title("treygolnik")
window.geometry('550x340')
window['bg'] = '#D8BFD8'

check = (window.register, "%P")

label = Label(window, text="Введите длины сторон треугольника", font="Times 18", bg='#D8BFD8', fg="Indigo")
label.pack()
label = Label(window, text="p.s числа должны содержать не больше 4 знаков:)", font="Times 15", bg='#D8BFD8', fg="Indigo")
label.pack()
lab1 = Label(window, fg="#E6E6FA", bg="#D8BFD8")
lab1.pack()

entry1 = Entry(window, font="Times 15", fg="SlateBlue", bg="Lavender", validate="key", validatecommand=check)
entry1.pack()
lab1 = Label(window, fg="#D8BFD8", bg="#D8BFD8")
lab1.pack()
entry2 = Entry(window, font="Times 15", fg="SlateBlue", bg="Lavender", validate="key", validatecommand=check)
entry2.pack()
lab1 = Label(window, fg="#D8BFD8", bg="#D8BFD8")
lab1.pack()
entry3 = Entry(window, font="Times 15", fg="SlateBlue", bg="Lavender", validate="key", validatecommand=check)
entry3.pack()
lab1 = Label(window, fg="#D8BFD8", bg="#D8BFD8")
lab1.pack()

check_button = Button(window, text="Результат", fg="Indigo", bg="#FFFF00", width=30, height=2, command=check_triangle)
check_button.pack()
lab1 = Label(window, fg="#D8BFD8", bg="#D8BFD8")
lab1.pack()

result_label = Label(window, text="", font="Times 15", fg="DarkSlateBlue", bg="#D8BFD8")
result_label.pack()


window.mainloop()


result_label = Label(window, text="", font="Times 15", fg="DarkSlateBlue", bg="#D8BFD8")
result_label.pack()


window.mainloop()
