import math


def add(x, y):
    return x + y


def produit(x, y):
    return x * y


def soustraire(x, y):
    return x - y


result = add(1, 2)
print(result)

sum = add

print(sum(3, 8))

print(add.__name__)
print(add.__doc__)


def my_map(func, arg1, arg2):
    res = []
    print(func.__name__)
    print("arg1: ", arg1)
    print("arg2: ", arg2)
    for i, j in zip(arg1, arg2):
        print(i, j)
        res.append(func(i, j))

    return res


a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

resultSum = my_map(add, a, b)
print(resultSum)

resulProduit = my_map(produit, a, b)
print(resulProduit)

resultSoustraire = my_map(soustraire, a, b)
print(resultSoustraire)


def calc_distance(_point1, _point2):
    # Extraction des coordonnées des points
    x1, y1, z1 = _point1
    x2, y2, z2 = _point2
    # Calcul de la distance entre point1 et point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    return distance


# Exemple d'utilisation avec deux points
# point1 = (1.0, 1.0, 1.0)
# point2 = (4.0, 4.0, 4.0)
# result = calc_distance(point1, point2)
# print(result)

point1 = [(1.0, 1.0, 1.0), (2.0, 2.0, 2.0), (3.0, 3.0, 3.0)]
point2 = [(4.0, 4.0, 4.0), (5.0, 5.0, 5.0), (6.0, 6.0, 6.0)]

resultCalcDistance = my_map(calc_distance, point1, point2)
print(resultCalcDistance)
