"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

We try to divide by a smaller prime number, if not divisible, we find the next one prime number through divisors of at
most rounded the root of the number. If it is divided entirely, we overwrite it, try to divide it entirely again,
if it does’t work, we are looking for the next one. So, until the result is 1. The last divisor is the maximum divisor.
The answer is 6857

--- 0.015 seconds --- (ryzen 2600)

Простые делители числа 13195 - это 5, 7, 13 и 29.
Каков самый большой делитель числа 600851475143, являющийся простым числом?

Пробуем разделить на меньшее простое число, если не делится, находим следующее простое число через делители не более
округленного корня числа. Если делится нацело, перезаписываем, пробуем разделить нацело еще раз, если не получается,
ищем следующее. Так, пока результат не будет 1. Последний делитель - максимальный делитель.
Ответ - 6857

--- 0.015 seconds --- (ryzen 2600)
"""

from math import sqrt
import time

start_time = time.time()

a = 600851475143
d = [2, 3]
n = 5
c = 0
while a > 1:
    while a % d[-1] != 0:
        while c <= sqrt(len(d)):
            if n % d[c] == 0:
                n += 2
                c = 1
            else:
                c += 1
        d.append(n)
        n += 2
        c = 1
    a = int(a / d[-1])
print(d[-1])

print("--- %s seconds ---" % (time.time() - start_time))
