# Task_3_1
chislo = int(input("Введите число ="))
print(chislo)
if chislo % 1000 == 0:
    print('Millennium')
else:
    print('Есть остаток, попробуйте другое число')

# Task_3_2
gosti = int(input("Введите число гостей ="))
print(gosti)
if gosti > 50:
    print('Необходим ресторан')
elif 20 < gosti < 50:
    print('Необходимо кафе')
else:
    print('Отмечайте дома')

# Task_3_3
stroka = str(input("Введите строку ="))
print(stroka)
if len(stroka) > 10:
    print('Длина строки больше 10 !!!')
else:
    print(stroka[2])

# Task_3_4
stroka = input("Введите строку: ")

dl_str = len(stroka)
ser_str = dl_str / 2
bukva_1 = (stroka[int(ser_str) - 1:int(ser_str)])
bukva_2 = (stroka[int(ser_str)])
if dl_str % 2 == 0:
    print('Центральная буква: ', bukva_1)
elif dl_str % 2 != 0:
    print('Центральная буква: ', bukva_2)

if bukva_1 == stroka[0]:
    print(stroka[0:-1])
elif bukva_2 == stroka[0]:
    print(stroka[0:-1])

# Task_3_5
from math import sqrt

perem_1_a = int(input("Введите первую переменную a ="))
perem_2_b = int(input("Введите вторую переменную b ="))
perem_3_c = int(input("Введите третью переменную с ="))
diskr = perem_2_b ** 2 - 4 * perem_1_a * perem_3_c
koren = (-perem_2_b) / (2 * perem_1_a)
print('Дискриминант: ', diskr)
if diskr < 0:
    print('Нет действительных корней, дискриминант меньше нуля')
elif diskr == 0:
    print('Единственный корень: ', koren)
elif diskr > 0:
    koren_1 = (-perem_2_b + sqrt(diskr)) / (2 * perem_1_a)
    print('Первый корень: ', koren_1)
    koren_2 = (-perem_2_b - sqrt(diskr)) / (2 * perem_1_a)
    print('Второй корень: ', koren_2)

# Task_3_6

pochta = str(input("Введите свою почту ="))
print(pochta)
if 'gmail.com' in pochta:
    print(pochta)
else:
    print('Проверьте свою почту')

