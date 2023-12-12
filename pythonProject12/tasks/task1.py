#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def is_balanced(string, index=0, open_count=0):
    if index == len(string):
        return open_count == 0

    current_char = string[index]

    if current_char == '(':
        return is_balanced(string, index + 1, open_count + 1)
    elif current_char == ')':
        return open_count > 0 and is_balanced(string, index + 1, open_count - 1)
    else:
        return is_balanced(string, index + 1, open_count)

if __name__ == '__main__':
    input_string = input("Введите строку: ")
    result = is_balanced(input_string)

    if result:
        print(f"Строка '{input_string}' сбалансированна.")
    else:
        print(f"Строка '{input_string}' не сбалансированна.")
