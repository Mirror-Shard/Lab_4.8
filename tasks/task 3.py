#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Напишите программу по описанию. Размеры многострочного текстового
поля определяются значениями, введенными в однострочные текстовые поля.
Изменение размера происходит при нажатии мышью на кнопку, а также при нажатии
клавиши Enter. Цвет фона экземпляра Text светлосерый ( lightgrey ), когда поле
не в фокусе, и белый, когда имеет фокус.
"""
from tkinter import *


def change(event=None):
    txt['width'], txt['height'] = ent1.get(), ent2.get()


def change_color(event, color):
    txt['bg'] = color


if __name__ == '__main__':
    root = Tk()

    f = Frame()
    ent1 = Entry(f, width=4)
    ent2 = Entry(f, width=4)
    Button(f, text="Изменить", command=change).pack(side=RIGHT)

    txt = Text(width=30, height=12, bg="Lightgrey")
    txt.bind("<FocusIn>", lambda e: change_color(e, "White"))
    txt.bind("<FocusOut>", lambda e: change_color(e, "Lightgrey"))

    f.pack()
    ent1.pack()
    ent2.pack()
    txt.pack()
    root.mainloop()
