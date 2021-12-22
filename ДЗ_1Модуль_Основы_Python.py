# 1задание
phrase_1 = 'Насколько проще было бы писать программы, если бы не заказчики'
phrase_2 = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'
if len(phrase_1) > len(phrase_2):
    print('Фраза 1 длиннее фразы 2')
elif len(phrase_2) > len(phrase_1):
    print('Фраза 2 длиннее фразы 1')
else:
    print('Фразы равной длины')

# 2задание
year = 2001
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0: # високосный год либо кратен 4, но при этом не кратен 100, либо кратен 400
    print('Високосный год')
else:
    print('Обычный год')

# 3задание
day = int(input('Введите день: '))
month = input('Введите месяц: ')
if (day >= 21 and month == 'Март') or (day <= 20 and month == 'Апрель'):
    print('Ваш знак зодиака: Овен')
elif (day >= 21 and month == 'Апрель') or (day <= 20 and month == 'Май'):
    print('Ваш знак зодиака: Телец')
elif (day >= 21 and month == 'Май') or (day <= 21 and month == 'Июнь'):
    print('Ваш знак зодиака: Близнецы')
elif (day >= 22 and month == 'Июнь') or (day <= 22 and month == 'Июль'):
    print('Ваш знак зодиака: Рак')
elif (day >= 23 and month == 'Июль') or (day <= 22 and month == 'Август'):
    print('Ваш знак зодиака: Лев')
elif (day >= 23 and month == 'Август') or (day <= 23 and month == 'Сентябрь'):
    print('Ваш знак зодиака: Дева')
elif (day >= 24 and month == 'Сентябрь') or (day <= 23 and month == 'Октябрь'):
    print('Ваш знак зодиака: Весы')
elif (day >= 24 and month == 'Октябрь') or (day <= 22 and month == 'Ноябрь'):
    print('Ваш знак зодиака: Скорпион')
elif (day >= 23 and month == 'Ноябрь') or (day <= 21 and month == 'Декабрь'):
    print('Ваш знак зодиака: Стрелец')
elif (day >= 22 and month == 'Декабрь') or (day <= 20 and month == 'Январь'):
    print('Ваш знак зодиака: Козерог')
elif (day >= 21 and month == 'Январь') or (day <= 18 and month == 'Февраль'):
    print('Ваш знак зодиака: Водолей')
elif (day >= 19 and month == 'Февраль') or (day <= 20 and month == 'Март'):
    print('Ваш знак зодиака: Рыбы')
else: 
    print('Данные введены некорректно')

# 4задание
width = 10
length = 205
height = 5
if width < 15 and length < 15 and height < 15:
    print('Коробка №1')
elif (width > 15 and width < 50) or (length > 15 and length < 50) or (height > 15 and height < 50):
    print('Коробка №2')
elif length > 200:
    print('Упаковка для лыж')
else:
    print('Стандартная коробка №3')

# 5задание
number = 123321
number_sign_6 = number % 10
number = number // 10
number_sign_5 = number % 10
number = number // 10
number_sign_4 = number % 10
number = number // 10
number_sign_3 = number % 10
number = number // 10
number_sign_2 = number % 10
number = number // 10
number_sign_1 = number % 10
if number_sign_1 + number_sign_2 + number_sign_3 == number_sign_4 + number_sign_5 + number_sign_6:
    print('Счастливый билет')
else:
    print('Несчастливый билет')

# 6задание
figure = input('Введите тип фигуры: ')
if figure == 'Круг':
    circle_radius = float(input('Введите радиус круга: '))
    area_of_a_circle = round(float(3.14 * (circle_radius ** 2)), 2)
    print('Площадь круга: ', area_of_a_circle)
elif figure == 'Треугольник':
    side_length_of_a_triangle_a = float(input('Введите длину стороны А: '))
    side_length_of_a_triangle_b = float(input('Введите длину стороны Б: '))
    side_length_of_a_triangle_c = float(input('Введите длину стороны С: '))
    half_perimeter = float((side_length_of_a_triangle_a + side_length_of_a_triangle_b + side_length_of_a_triangle_c) / 2)
    area_of_a_triangle = round(float((half_perimeter * (half_perimeter - side_length_of_a_triangle_a) * (half_perimeter - side_length_of_a_triangle_b) * (half_perimeter - side_length_of_a_triangle_c)) ** 0.5), 2)
    print('Площадь треугольника: ', area_of_a_triangle)
elif figure == 'Прямоугольник':
    rectangle_length = float(input('Введите длину прямоугольника: '))
    rectangle_width = float(input('Введите ширину прямоугольника: '))
    rectangle_width = round(float(rectangle_length * rectangle_width), 2)
    print('Площадь прямоугольника: ', rectangle_width)
    
        


    









    


