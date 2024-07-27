import math

print("Вітаємо у калькуляторі")

n1 = int(input("Введіть перше число:"))

operation = input("Виберіть дію (+, -, *, /): ")

n2 = int(input("Введіть друге число:"))

def calculate(n1,operation,n2):
    if operation == "+":
        return n1 + n2
    elif operation == "-":
        return n1 - n2
    elif operation == "*":
        return n1 * n2
    elif operation =="/":
        if n2 == 0:
            return "Увага! Дільник не може дорівнювати 0!"
        return n1 / n2

result = calculate(n1,operation, n2)

print(f"Відповідь: {result}")