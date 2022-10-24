#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Напишите программу, состоящую из двух списков Listbox . В первом будет,
например, перечень товаров, заданный программно. Второй изначально пуст,
пусть это будет перечень покупок. При клике на одну кнопку товар должен
переходить из одного списка в другой. При клике на вторую кнопку возвращаться
(человек передумал покупать). Предусмотрите возможность множественного выбора
элементов списка и их перемещения.
"""
from tkinter import *


def move():
    select = list(box1.curselection())
    # Добавляет выбранные во 2-й список
    for i in select:
        box2.insert(END, box1.get(i))
    select.reverse()
    # Удаляет выбранные
    for i in select:
        box1.delete(i)


def back():
    select = list(box2.curselection())
    # Добавляет выбранные в 1-й список
    for i in select:
        box1.insert(END, box2.get(i))
    # Удаляет выбранные
    select.reverse()
    for i in select:
        box2.delete(i)


if __name__ == '__main__':
    root = Tk()
    products = ["apple", "bananas", "carrot", "bread",
                "butter", "meat", "potato", "pineapple"]
    # Список слева
    box1 = Listbox(selectmode=EXTENDED)
    for i in products:
        box1.insert(0, i)
    # Фрейм с кнопками
    f = Frame()
    Button(f, text=">>>", width=6, command=move).pack()
    Button(f, text="<<<", width=6, command=back).pack()
    # Список справа
    box2 = Listbox(selectmode=EXTENDED)

    box1.pack(side=LEFT)
    f.pack(side=LEFT)
    box2.pack(side=LEFT)
    root.mainloop()
