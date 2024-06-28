def print_params(a = 1, b = 'Июнь', c = True): # 1) Функция с параметрами по умолчанию
    print(a, b, c)

print_params()
print_params(a = 2, b = 'Yellow')
print_params(a = False)
print_params(b = 25, c = [1, 2, 3])

values_list = [1, 'Name', True] # 2) Распаковка параметров
values_dict = {'a': 35, 'b': 'Биржа', 'c': False }

print_params(*values_list)

print_params(**values_dict)

values_list_2 = ['Долото', {1,2}] #3) Распаковка + отдельные параметры
print_params(values_list_2, 42)