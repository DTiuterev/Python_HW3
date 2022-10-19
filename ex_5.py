#5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
x = int(input('Введите любое натуральное число, я составлю список Фибоначчи, в т.ч. для отрицательных индексов:\n'))

def Fibonacci(n):
    if n in [1, 2]:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

def NegaFibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, n):
            num1, num2 = num2, num1 - num2
        return num2

list = [0]
for i in range(1, x + 1):
    list.append(Fibonacci(i))
    list.insert(0, NegaFibonacci(i))

print(f'Список Фибоначчи, в т.ч. для отрицательных индексов:\n{list}')