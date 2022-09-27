x=input("введите x: ")
y=input("введите y: ")
def prim(a,b):
    try:
        s=a//b
    except ZeroDivisionError as z:
        s=z
    except ValueError as v:
        s = v
    except TypeError as t:
        s = t
    else:
        print("Сработало else")
        s=a+b
        print(s)
    finally:
        print("Даже если в конструкции ошибка то вывод будет.")
        x = 0.12
        print(x)
    print(s)
prim(x,y)
