# 1.1 Дан произвольный список, содержащий только числа. Выведите результат сложения всех чисел больше 10
def greater_10(lst):
	total = 0
	for el in lst:
		if el > 10:
			total += el
	return total

lst = [1, 22, 19, 3, 4, 7, 9, 2, 2]
print(greater_10(lst))


# 1.2 Пусть задан список, содержащий строки. Выведите все строки, заканчивающиеся буквой r
def end_r(lst):
	lst_r = []
	for el in lst:
		if el[-1] == 'r':
			lst_r.append(el)
	return lst_r

lst = ['roar', 'tasty carrot', 'rrr', 'r', 'mauntain road', 'red tomato']
print(end_r(lst))


# 1.3 Сгенерируйте и выведите cлучайную строку размером 6 символов, содержащую только цифры. Строка должна содержать хотя бы одну цифру 3
import string
import random

def generator(size=6, chars=string.digits):
	my_str = list(random.choice(chars) for _ in range(size))
	my_str[random.randint(0, size)] = '3'
	return ''.join(my_str)

print(generator())


# 1.4 Пусть дана строка произвольной длины. Выведите информацию о том, сколько в ней символов и сколько слов
def str_info(s):
	n_symb = len(s)
	n_words = len(s.strip().split(' '))
	return (n_symb, n_words)

s = ' Пусть дана строка произвольной длины '
print("Символов: %s, слов: %s" % str_info(s))


# 2.1 Пусть дана матрица чисел размером NхN. Представьте данную матрицу в виде списка. Выведите результат сложения всех элементов матрицы

def matrix_sum(matrix):
	m_list = list()
	for line in matrix:
		for el in line:
			m_list.append(el)
	return sum(m_list)

matrix = [[1, 2, 3], [9, 2, 2], [7, 2, 3]]
print(matrix_sum(matrix))


# 2.2 Дана матрица размером NxM. Напишите алгоритм вычисления максимума из сумм элементов каждого столбца
def max_column(matrix):
	max_col = 0
	for i in range(len(matrix[0])):
		sum_col = 0
		for line in matrix:
			sum_col += line[i]
		if sum_col > max_col:
			max_col = sum_col
	return max_col

matrix = [	[1, 2, 12], 
			[9, 2, 2], 
			[7, 2, 3], 
			[1, 1, 9] ]

print(max_column(matrix))


# 3.1 Пусть список студентов представлен в виде структуры [[No, ФИО, Возраст,Группа],[No, ФИО, Возраст, Группа],[No, ФИО, Возраст, Группа]]
# Преобразуйте список в словарь вида: {No: [ФИО, Возраст, Группа], No:[....], No: [....]}

def student_dict(s_list):
	s_dict = dict()
	for line in s_list:
		# s_dict.update({line[0]: line[1:]})
		s_dict[line[0]] = line[1:]
	return s_dict

students = [[1, 'A B', 20, 'M13'], [2, 'C D', 19, 'M12'], [3, 'E F', 21, 'M13']]
print(student_dict(students))


# 3.2 Напишите алгоритм, позволяющий найти запись в словаре из задачи 3.1 (без преобразования словаря обратно в список) по фамилии
# и изменить в ней номер группы. Фамилию и новый номер группы необходимо ввести с клавиатуры
def change_group(s_dict, fio=None, new_group=None):
	if fio is None:
		fio = input("Enter fio: ")
	if new_group is None:
		new_group = input("Enter new group: ")
	for i in s_dict:
		if s_dict[i][0] == fio:
			s_dict[i][2] = new_group

	return s_dict

s_dict = student_dict(students)
change_group(s_dict)
