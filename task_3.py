# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

x = int(input('Введите Х не равный 0: '))
y = int(input('Введите Y не равный 0: '))
if x == 0 or y == 0:
	print('Вы ввели значение равное 0')
else:
	if x > 0 and y > 0:
		print('x =', x, 'y =', y, ' -> 1')
	elif x > 0 and y < 0:
		print('x =', x, 'y =', y, ' ->  4')
	elif x < 0 and y > 0:
		print('x =', x, 'y =', y, ' ->  2')
	elif x < 0 and y < 0:
		print('x =', x, 'y =', y, ' ->  3')
