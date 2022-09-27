def ugol(*storona):
    pl = (pow(a, 2) * pow(3, 0.5)) / 4
    p=3*a
    return p, pl
a = int(input("Введите сторону: "))

print("У равностороннего теугольника следущие параметры:",ugol(a))