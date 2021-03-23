"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

Iterate through all numbers from 1 to 1000 (without 1000). We sum up if the number is a multiple of 3 or 5.
The answer is 233168

--- 0.0 seconds --- (ryzen 2600)

Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
Найдите сумму всех чисел меньше 1000, кратных 3 или 5.

Перебор всех чисел от 1 до 1000 (без 1000). Суммируем, если число кратно 3 или 5.
Ответ - 233168

--- 0.0 seconds --- (ryzen 2600)
"""

import time

start_time = time.time()

print(sum(a for a in range(1000) if a % 3 == 0 or a % 5 == 0))

print("--- %s seconds ---" % (time.time() - start_time))
