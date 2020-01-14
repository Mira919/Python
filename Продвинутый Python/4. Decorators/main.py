# Написать декоратор. Он записывает в файл дату и время вызова функции, имя функции, аргументы, с которыми вызвалась и возвращаемое значение.
# Написать декоратор из п.1, но с параметром – путь к файлу (параметризованный декоратор).
# Применить написанный декоратор к приложению из любого предыдущего д/з

# Данная функция возвращает генератор из лекции 2. Если этот пример плохой, я закоментил еще одну функцию суммирования ниже, можно на ней проверить
import datetime
import hashlib

def parametrize_decor(name_file):
	def decor(old_func):
		def new_func(*args, **kwargs):
			result = old_func(*args, **kwargs)
			func_time = 'Время вызова функции - ' + str(datetime.datetime.now())
			func_name = 'Имя вызванной функции - ' + old_func.__name__
			func_arg = 'Аргументы вызванной функции - ' + str(args) + str(kwargs)
			func_res = 'Результат вызванной функции - ' + str(result)
			with open(name_file, 'w') as f:
				f.write(func_time + '\n' + func_name + '\n' + func_arg + '\n' + func_res)
			return result
		return new_func
	return decor

@parametrize_decor('test.txt')
def generator(file):
    with open(file, 'r') as f:
        for line in f:
            str = line.encode('utf-8')
            hash_str = hashlib.md5(str)
            yield hash_str.hexdigest()

for hash_str in generator('Python.txt'):
    print(hash_str)

# @parametrize_decor('test.txt')
# def sum(x, y):
# 	return x + y
#
# print(sum(2, 3))
