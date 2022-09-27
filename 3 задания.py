n,m = int(input("Введите n элементов массива: ")), int(input("Введите m элементов массива: "))
arr = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        arr[i][j] = int(input("Введите число: "))


def out():
    for count in arr:
        print(' '.join([str(elem) for elem in count]))
    return


out()


def zam():
    global flag
    flag=0
    a = int(input("Введите 1 - е число для замены: "))
    b = int(input("Введите 2 - е число для замены: "))

    for i in range(n):
        try:
            z = arr[i][a]
            arr[i][a] = arr[i][b]
            arr[i][b] = z
        except IndexError:
            flag = 1
            print("Не верно введены индексы")
            break
    if flag == 0:
        out()
        print("ALL DONE !")
    return

zam()
if flag == 1:
    key = input("Хотите ли вы ввсети новые числа для замены ? (y/n):")
    if key == 'y':
        zam()
    else:
        print("Good Bye ♥️")