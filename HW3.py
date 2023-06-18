# ✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию).

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()

# Печать первых 10 чисел Фибоначчи
for _ in range(10):
    print(next(fib))
