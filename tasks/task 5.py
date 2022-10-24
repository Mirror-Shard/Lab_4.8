#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Изучите приведенную программу и самостоятельно запрограммируйте постепенное
движение фигуры в ту точку холста, где пользователь кликает левой кнопкой мыши
Координаты события хранятся в его атрибутах x и y ( event.x , event.y )
"""
from tkinter import *


def motion(event):
    # Центр круга
    x, y = c.coords(ball)[0]+20, c.coords(ball)[1]+20
    # Перемещение х на 1
    if x < event.x:
        c.move(ball, 1, 0)
    elif x > event.x:
        c.move(ball, -1, 0)
    # Перемещение y на 1
    if y < event.y:
        c.move(ball, 0, 1)
    elif y > event.y:
        c.move(ball, 0, -1)
    # Рекурсия
    if [c.coords(ball)[0], c.coords(ball)[1]] != [event.x, event.y]:
        root.after(10, lambda: motion(event))


if __name__ == '__main__':
    root = Tk()

    c = Canvas(root, width=300, height=200, bg="white")
    c.pack()
    ball = c.create_oval(0, 100, 40, 140, fill='green')
    c.bind("<Button-1>", motion)

    root.mainloop()
