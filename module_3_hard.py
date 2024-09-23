data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(*args):
    numbers = 0
    strings = 0

    def calc(data_):
        nonlocal numbers, strings
        if isinstance(data_, list) or isinstance(data_, tuple) or isinstance(data_, set):
            for item in data_:
                calc(item)
        elif isinstance(data_, dict):
            for value in data_.values():
                calc(value)
            for key in data_.keys():
                calc(key)
        elif isinstance(data_, int) or isinstance(data_, str):
            if isinstance(data_, int):
                numbers += data_
            elif isinstance(data_, str):
                strings += len(data_)

    calc(data_structure)
    return numbers + strings


result = calculate_structure_sum(data_structure)
print(result)
