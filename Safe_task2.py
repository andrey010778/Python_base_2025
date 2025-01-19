import math


def input_param():
    d1 = float(input("Введите расстояние от спасателя до кромки воды в ярдах:"))
    d2 = float(input("Кратчайшее расстояние от утопающего до берега, в футах: "))
    h = float(input("Боковое смещение между спасателем и утопающим, в ярдах: "))
    vsand = float(input("Скорость движения по песку, в милях в час: "))
    n = float(input("Коэффициент замедления спасателя при движении по воде: "))
    theta = float(input("Направление движения спасателя по песку, в градусах:"))
    return d1, d2, h, vsand, n, theta


def angle():
    d1, d2, h, vsand, n, theta = input_param()
    theta1 = math.tan(theta * math.pi / 180)
    x = d1 * 3 * theta1

    l1 = math.sqrt(x ** 2 + d1 ** 2)
    l2 = math.sqrt((h * 3 - x) ** 2 + d2 ** 2)

    t = (1 / (vsand * 5280) * (l1 + n * l2)) * 3600
    return t


print(angle())