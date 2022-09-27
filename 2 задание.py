def vvod_int():
    l = int(input("Введите число: "))
    nada(l)
    return
def vvod_spis():
    print('Вводите значения, нажимайте enter')
    print('для окончания ввода просто нажмите enter')
    a = int(input('-->> '))
    words = []
    while True:
        try:
            words.append(a)
            a = int(input('-->> '))
        except:
            break
    print(words)
    nada(words)
    return
def vvod_str():
    string=input("Введите строку: ")
    print(string)
    nada(string)
def vvod_mn():
    print('Вводите значения, нажимайте enter')
    print('для окончания ввода просто нажмите enter')
    a = int(input('-->> '))
    mn = set([])
    while True:
        try:
            mn.add(a)
            a = int(input('-->> '))
        except:
            break
    print(mn)
    nada(mn)
def nada(per):
    if (isinstance(per, list)):
        while True:
            print("\nВыберите\n1. Вывод всех чётных чисел\n2. Найти сумму после второго отрицательного  элемента\n3. Выход")
            key = int(input("Ваш выбор: "))
            if key==1:
                for i in per:
                    try:
                        if i % 2 == 0:
                            print(i,end=' ')
                    except IndexError:
                        print("Inxex ")
            elif key==2:
                flag = 0
                counter = 0
                for i in per:
                    if i < 0:
                        flag += 1
                        if flag <= 2:
                            continue
                    if flag >= 2:
                        counter += i
                print(counter)
            elif key==3:
                False
                break
            else: print("Не правельный ввод")
    if type(per) is int:
        flag = 0
        for i in range(per+1):
            if i == 2 or i == 3 or i == 5 or i == 7:
                print(i, end=' ')
                flag = 1
            if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
                print(i, end=' ')
                flag = 1
        if flag == 0:
            print("Простых чисел в данном диапозоне нет")
    if type(per) == str:
        print("Ваша строка после конвертации:", per.split())
    if (isinstance(per, set)):
        m=min(per)
        x=max(per)
        print("Минимальный элемент:",m,"Максимальный элемент:",x)
    return
while True:
    count=int((input("\nВыберите\n1. Ввод списка\n2. Ввод числа\n3. Ввод строки\n4. Ввод множества\n5. Выход\nВаш выбор: ")))
    if count == 1:
        vvod_spis()
    elif count == 2:
        vvod_int()
    elif count == 3:
        vvod_str()
    elif count == 4:
        vvod_mn()
    else:
        False
        break