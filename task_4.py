# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных 
# координат точек в этой четверти (x и y).

num = input('Введите номер четверти (1, 2, 3 или 4): ')
if num == '1':
	print('X положительный, Y положительный')
elif num == '2':
	print('X отрицательный, Y положительный')
elif num == '3':
	print('X отрицательный, Y отрицательный')
elif num == '4':
	print('X положительный, Y отрицательный')
else: print('Вы ввели некорректный номер четверти')
