import sys


# непосредственно реализация алгоритма
def karatsuba_multiplication(x, y):
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    half = n // 2

    # разделение числа на две равные по длине (или практически равные в случае нечетной длины) части
    # пример: х = 123456 => high1 = 123, low1 = 456
    high1, low1 = divmod(x, 10 ** half)
    high2, low2 = divmod(y, 10 ** half)

    # рекурсивные вызовы и деление чисел до случая x < 10 | y < 10
    z0 = karatsuba_multiplication(low1, low2)
    z1 = karatsuba_multiplication((low1 + high1), (low2 + high2))
    z2 = karatsuba_multiplication(high1, high2)

    # в данном случае z0 - "левая" часть, z2 - "правая" часть, а
    # z1 - сумма всех частей => z1 - z0 - z2 - "средняя" часть
    return (z2 * 10 ** (2 * half)) + ((z1 - z2 - z0) * 10 ** half) + z0


while True:
    try:
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))

        result = karatsuba_multiplication(num1, num2)

        print("Результат умножения:", result)
        print("Нажмите любую клавишу для выхода...")
        sys.stdin.read(1)
        sys.exit(1)
    except ValueError:
        print("Ошибка: Введите целочисленные значения.")


