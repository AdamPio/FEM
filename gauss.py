def func(x):
    return 5 * x ** 2 + 3 * x + 6


def func2(x, y):
    return 5 * x ** 2 * y ** 2 + 3 * x * y + 6


def d1_2():
    suma = 0
    w = [-1 / (3 ** (1 / 2)), 1 / (3 ** (1 / 2))]
    A = [1, 1]
    for i in range(2):
        suma += A[i] * func(w[i])

    return suma


def d1_3():
    suma = 0
    w = [-(3 / 5) ** (1 / 2), 0, (3 / 5) ** (1 / 2)]
    A = [5 / 9, 8 / 9, 5 / 9]
    for i in range(3):
        suma += A[i] * func(w[i])

    return suma


def d2_2():
    suma = 0
    E = [-1 / (3 ** (1 / 2)), 1 / (3 ** (1 / 2))]
    N = [-1 / (3 ** (1 / 2)), 1 / (3 ** (1 / 2))]
    A = [1, 1]
    for i in range(2):
        for j in range(2):
            suma += A[i] * A[j] * func2(E[i], N[j])

    return suma


def d2_3():
    suma = 0
    w = [5 / 9, 8]
    E = [-(3 / 5) ** (1 / 2), 0, (3 / 5) ** (1 / 2)]
    N = [-(3 / 5) ** (1 / 2), 0, (3 / 5) ** (1 / 2)]
    A = [5 / 9, 8 / 9, 5 / 9]
    for i in range(3):
        for j in range(3):
            suma += A[i] * A[j] * func2(E[i], N[j])

    return suma
