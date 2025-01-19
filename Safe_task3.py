'''Ввод значений из консоли не делается, параметры задаются внутри функции'''


import math


def min_time():
    theta = []
    for i in range(1, 91, 1):
        theta.append(i)

    tlist = []
    for i in theta:
        d1 = 8
        d2 = 10
        h = 50
        v_sand = 5
        n = 2

        theta1 = math.tan(i * math.pi / 180)
        x = d1 * 3 * theta1

        l1 = math.sqrt(x ** 2 + d1 ** 2)
        l2 = math.sqrt((h * 3 - x) ** 2 + d2 ** 2)

        t = (1 / (v_sand * 5280) * (l1 + n * l2)) * 3600
        tlist.append(t)

        z = min(tlist)
    return z


print(min_time())