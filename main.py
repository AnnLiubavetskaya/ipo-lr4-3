n = int(input("Введите число n: "))
num = 1
for i in range(1, n + 1):
    num *= i

print(f"Произведение чисел от 1 до {n} равно {num}.")
