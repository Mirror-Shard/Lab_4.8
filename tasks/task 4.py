#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Решите задачу: Создайте на холсте подобное изображение
"""
from tkinter import *


if __name__ == '__main__':
    root = Tk()

    root.geometry('500x500')

    c = Canvas(root, width=500, height=500, bg='white')
    c.pack()

    c.create_oval(350, 20, 450, 120, fill="Orange", outline="White")
    c.create_polygon(
        (250, 80), (350, 180),
        (300, 180), (300, 380),
        (200, 380), (200, 180),
        (150, 180),
        fill='Lightblue'
    )

    x = 0
    while x < 500:
        c.create_arc(x, 555, x + 90, 450,
                     start=180, extent=-80,
                     style=ARC, width=3, outline='green')
        x += 15

    root.mainloop()
