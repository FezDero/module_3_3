#  1-ая часть задачи: функция с параметрами по умолчанию:
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(1 , 4, 5)

print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])
print_params(a = 11, b = 'число', c = False)

# 2-ая часть задачи: Распаковка параметров:

values_list = [2, 'string', False]
values_dict = {'a':1, 'b':'строка', 'c':True}

print_params(*values_list)
print_params(**values_dict)

# 3-ая часть задачи: Распаковка + отдельные параметры:
values_list_2 = ['int', 32]

print_params(*values_list_2, 42)





