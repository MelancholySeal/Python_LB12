#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit
from functools import lru_cache
import matplotlib.pyplot as plt
import numpy as np

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

@lru_cache(maxsize=None)
def factorial_recursive_cached(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive_cached(n - 1)

def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

@lru_cache(maxsize=None)
def fib_recursive_cached(n):
    if n <= 1:
        return n
    return fib_recursive_cached(n - 1) + fib_recursive_cached(n - 2)

def measure_time(func, *args):
    return timeit.timeit(lambda: func(*args), number=100)

def plot_results(x, y, label, subplot):
    plt.subplot(subplot)
    plt.scatter(x, y, label=label)
    plt.xlabel('Эксперимент')
    plt.ylabel('Время (секунды)')
    plt.title(f'Сравнение времени - {label}')
    plt.legend()


if __name__ == '__main__':
    experiments = 30
    values = np.arange(1, 11)

    factorial_iterative_times = [measure_time(factorial_iterative, n) for n in values]
    factorial_recursive_times = [measure_time(factorial_recursive, n) for n in values]
    factorial_recursive_cached_times = [measure_time(factorial_recursive_cached, n) for n in values]

    fib_iterative_times = [measure_time(fib_iterative, n) for n in values]
    fib_recursive_times = [measure_time(fib_recursive, n) for n in values]
    fib_recursive_cached_times = [measure_time(fib_recursive_cached, n) for n in values]

    plt.figure(figsize=(15, 10))

    plot_results(values, factorial_iterative_times, 'Итеративный - Факториал', 231)
    plot_results(values, factorial_recursive_times, 'Рекурсивный - Факториал', 232)
    plot_results(values, factorial_recursive_cached_times, 'Рекурсивный - Факториал (Cached)', 233)

    plot_results(values, fib_iterative_times, 'Итеративный - Фибоначчи', 234)
    plot_results(values, fib_recursive_times, 'Рекурсивный - Фибоначчи', 235)
    plot_results(values, fib_recursive_cached_times, 'Рекурсивный - Фибоначчи (Cached)', 236)

    plt.tight_layout()
    plt.show()
