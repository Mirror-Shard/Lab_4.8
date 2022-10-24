#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Напишите программу по следующему описанию. Нажатие Enter в однострочном
текстовом поле приводит к перемещению текста из него в список (экземпляр
Listbox). При двойном клике ( <Double-Button-1> ) по элементу-строке списка,
она должна копироваться в текстовое поле.
"""
from tkinter import *


def add(event):
    box.insert(END, ent.get())
    ent.delete(0, END)


def copy(event):
    select = list(box.curselection())
    ent.insert(END, box.get(select))


if __name__ == '__main__':
    root = Tk()

    ent = Entry(width=20)
    ent.bind("<Return>", add)

    box = Listbox(selectmode=EXTENDED)
    box.bind("<Double-Button-1>", copy)

    ent.pack(pady=10, padx=10)
    box.pack(pady=10)
    root.mainloop()
