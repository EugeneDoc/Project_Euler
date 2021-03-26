"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
is 9009 = 91 × 99. Find the largest palindrome made from the product of two 3-digit numbers.

Search for the first palindrome - the square of numbers to establish the minimum. Further, direct search with constant
limiting the minimum.
The answer is 913 * 993 = 906609

--- 0.0 seconds --- (ryzen 2600)

Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.
Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.

Поиск первого палиндрома - квадрата чисел для установления минимума. Далее прямой перебор с постоянным
ограничением минимума.
Ответ - 913*993=906609

--- 0.0 seconds --- (ryzen 2600)
"""
import time

start_time = time.time()

"""
The function of checking a number for palindromicity.
Фукция проверки числа на палиндромность.
"""


def pal(n):
    old = n
    new = 0
    while n > 0:
        new = new * 10 + n % 10
        n //= 10
    if old == 0:
        return 0
    elif new == old:
        return 1
    else:
        return 0


"""
Quick search for the first palindrome through the square of a three-digit number.
Быстрый поиск первого палиндрома через квадрат трёхзначного числа.
"""


def fm(a):
    while a >= 100:
        while pal(a ** 2) != 1:
            a -= 1
        if a == 100:
            return 100
        else:
            return a


minim = fm(999)
"""
Recording the first result.
Запись первого результата.
"""
if minim != 100:
    res = [minim, minim, minim ** 2]
else:
    res = [999, 999, 999 ** 2]
    minim = 999

"""
Enumeration of all multipliers to search for a palindrome with updating the minimum.
Перебор всех множетелей на поиск полиндрома с обновлением минимума.
"""
minim = minim ** 2 // 999
n1 = 999
n2 = 999
while n2 > minim:
    while n1 > minim:
        if pal(n1 * n2) == 1:
            if n1 * n2 > res[-1]:
                res = [n1, n2, n1 * n2]
                minim = res[-1] / 999
        n1 -= 1
    n2 -= 1
    n1 = n2 - 1

print(res)

print("--- %s seconds ---" % (time.time() - start_time))
