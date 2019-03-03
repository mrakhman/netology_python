# Простые задания

""" 
1. Даны 2 строки long_phrase и short_phrase. Напишите код, который проверяет,
действительно ли длинная фраза long_phrase длиннее короткой short_phrase. 
И выводит True или False в зависимости от результата сравнения.
"""
long_phrase = 'Насколько проще было бы писать программы, если бы не заказчики'
short_phrase = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'
print (len(long_phrase) > len(short_phrase))



"""
2. Дана строка text. Определите какая из двух букв встречается в нем чаще - 'а' или 'и'.
text = 'Если программист в 9-00 утра на работе, значит, он там и ночевал'
P.S. Вам может помочь метод replace.
"""
text = 'Если программист в 9-00 утра на работе, значит, он там и ночевал'
# 1 способ - с помощью replace
if (len(text.replace('а','')) < len(text.replace('и',''))):
    print("Букв 'а' больше")
else:
    print("Букв 'и' больше")

# 2 способ - с помощью count
if (text.count('а') > text.count('и')):
    print("Букв 'а' больше")
else:
    print("Букв 'и' больше")



"""
3. Дано значение объема файла в байтах. Напишите перевод этого значения в мегабайты в формате:
'Объем файла равен 213.68Mb'
P.S. Найдите определение килобайта. Это не 1000 байт.
"""
# 1kb = 1024 byte; 1Mb = 1 048 576 byte (1024^2)
# 1 - Using function
def n_megabyte(n_byte):
	n_mb = n_byte * 1.0 / 1048576
	return ('Объем файла равен {:.2f}Mb'.format(n_mb))

n_megabyte(724288)

# 2 - Using 'print'
n_byte = 724288
n_mb = n_byte / 1048576
print ('Объем файла равен {:.2f}Mb'.format(n_mb))



"""
4. Выведите на экран значение синуса 30 градусов с помощью метода math.sin
"""
import math

math.sin(math.radians(30))



"""
5. В прошлом задании у вас скорее всего не получилось точного значения 0.5 
из-за конечной точности вычисления синуса. Но почему некоторые простые операции 
также могут давать неточный результат? 
Попробуйте вывести на экран результат операции 0.1 + 0.2
Почему результат неточен?
"""