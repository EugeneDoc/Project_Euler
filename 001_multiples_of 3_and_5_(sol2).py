"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

Sum up all the numbers starting from 3 with step 3 up to 1000.
Sum up all numbers from 5 with step 5, but we skip every 3rd, because it is a multiple of 3.
This solution works faster than the first one, there is not a single division operation, we only summarize.
The answer is 233168


--- 0.0 seconds --- (ryzen 2600)

Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
Найдите сумму всех чисел меньше 1000, кратных 3 или 5.

Суммируем все числа начиная с 3 с шагом 3 до 1000.
Суммируем все числа от 5 с шагом 5, но каждое 3е пропускаем, т.к. оно кратно 3.
Это решение работает быстрее первого, нет ни одной операции деления, только суммируем.
Ответ - 233168

--- 0.0 seconds --- (ryzen 2600)
"""

import time

start_time = time.time()

ans = 0
a = 3
while a < 1000:
    ans += a
    a += 3

b = 5
c = 0
while b < 1000:
    if c < 2:
        ans += b
        b += 5
        c += 1
    else:
        b += 5
        c = 0

print(ans)

print("--- %s seconds ---" % (time.time() - start_time))
