# 3. Создайте функцию генератор чисел Фибоначчи (см. Википедию)

n = 10

fib = lambda n: fib(n - 1) + fib(n - 2) if n > 2 else 1
res = [fib(n) for n in range(n)]
print(res)
