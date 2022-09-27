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
print()
