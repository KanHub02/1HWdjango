# Попробывал создать опрос, "пользователь получает информацию о погоде"
# batken = '3°C'
# naryn = '-6°C'
# bishkek = '5°C'
# jld = '7°C'
# osh = '5°C'
# talas = '3°C'
# IK = '-2°C'
# ask = input('Укажите область!')
# if ask == 'Ош':
#     print(f'Температура в Оше {osh}')
# if ask == 'Бишкек':
#     print(f'Температура в Бишкеке {bishkek}')
# if ask == 'Джалал-Абад':
#     print(f'Температура в Джалал-Абаде {jld}')
# if ask == 'Баткен':
#     print(f'Температура в Баткене {batken}')
# if ask == 'Талас':
#     print(f'Температура в Таласе {talas}')
# if ask == 'Иссык-Куль':
#     print(f'Температура на Иссык-Куле {IK}')
# if ask == 'Нарын':
#     print(f'Температура в Нарыне {naryn}')
# ask2 = input('Хотите узнать о погоду в других областях?')
# if ask2 == 'Да':
#     print('Хорошо, начните программу заново!')
# if ask2 == 'Нет':
#     print('Хорошо, до свидания!')


# Узнаем среднию температуру воздуха в КР
print('Нам нужно узнать средний показатель температуры воздуха в КР')
print('Укажите температуру каждой области')
# Температура каждой области вводиться пользователем по запросу программы
bishkek = int(input('Bishkek'))
naryn = int(input('Naryn'))
osh = int(input('Osh'))
IK = int(input('Issyk-Kol'))
talas = int(input('Talas'))
batken = int(input('batken'))
JalalAbad = int(input('JalalAbad'))
# находим ср. показатель
average = (bishkek + naryn + osh + IK + talas + batken + JalalAbad)/ 7
# print(f'Средний показатель температуры воздуха по КР на сегодня {average}°C')
print('Средний показатель температуры воздуха по КР на сегодня',"%.1f" % average,'°C')
# Задание выполнено, нужно разобрать "%.1f" % average(не понятно)















