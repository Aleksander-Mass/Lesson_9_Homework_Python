import cmath

# 1. Нахождение корней квадратного уравнения:
def quadratic_solver(a, b, c):
    D = cmath.sqrt(b**2 - 4*a*c)
    x1 = (-b + D) / (2 * a)
    x2 = (-b - D) / (2 * a)
    return (x1, x2)


# 2. Генерация csv файла с тремя случайными числами в каждой строке (100-1000 строк):
import csv
import random

def generate_csv(filename, min_rows=100, max_rows=1000):
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for _ in range(random.randint(min_rows, max_rows)):
            row = [random.randint(1, 100) for _ in range(3)]
            csvwriter.writerow(row)


# 3. Декоратор для нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла:
import functools

def process_csv(filename):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with open(filename, 'r') as csvfile:
                csvreader = csv.reader(csvfile)
                for row in csvreader:
                    a, b, c = map(int, row)
                    result1, result2 = func(a, b, c)
                    print(f"Корни квадратного уравнения с коэффициентами {a}, {b}, {c}: {result1}, {result2}")
        return wrapper
    return decorator

# 4. Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл:
import json

def save_to_json(filename):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            x1, x2 = func(*args, **kwargs)
            data = {
                "function": func.__name__,
                "arguments": args,
                "x1": str(x1),
                "x2": str(x2)
            }
            with open(filename, 'w') as json_file:
                json.dump(data, json_file)
            return (x1, x2)
        return wrapper
    return decorator

#####

# Tests
@process_csv('random_numbers.csv')
@save_to_json('results.json')
def solve_and_log(a, b, c):
    return quadratic_solver(a, b, c)

generate_csv('random_numbers.csv')
solve_and_log()


