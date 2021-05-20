#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    S = input("Введите ваш текст: ")
    f = max(S.split(), key=len)
    print("Самое длинное слово в предложении: ", f)