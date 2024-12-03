def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [2, 'список', False]
values_dict = {'a':3, 'b':'словарь', 'c':None }

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [4, 'еще список']
print_params(*values_list_2, 42)