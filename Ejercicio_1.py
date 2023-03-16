def devolver_distintos(n1, n2, n3):
    suma = n1 + n2 + n3
    if suma > 15:
        devolver = max(n1, n2, n3)
    elif suma < 10:
        devolver = min(n1, n2, n3)
    else:
        if n3 >= n1 >= n2 or n2 >= n1 >= n3:
            devolver = n1
        elif n3 >= n2 >= n1 or n1 >= n2 >= n3:
            devolver = n2
        else:
            devolver = n3
    return devolver

print(devolver_distintos(3, 6, 4))
