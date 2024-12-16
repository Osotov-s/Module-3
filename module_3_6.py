data_structure = [

  [1, 2, 3],

  {'a': 4, 'b': 5},

  (6, {'cube': 7, 'drum': 8}),

  "Hello",

  ((), [{(2, 'Urban', ('Urban2', 35))}])

]

def sum_data_structure(*args):
    sum = 0
    for i in args:
        if isinstance(i, str):
            sum += len(i)

        elif isinstance(i, int):
            sum += i

        elif isinstance(i, float):
            sum += i

        elif isinstance(i, list):
            sum += sum_data_structure(*i)

        elif isinstance(i, dict):
            sum += sum_data_structure(*tuple(i.items()))

        elif isinstance(i, tuple):
            sum += sum_data_structure(*i)

        elif isinstance(i, set):
            sum += sum_data_structure(*i)

    return sum

result = sum_data_structure(data_structure)
print(result)
