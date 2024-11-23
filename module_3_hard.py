
def calculate_structure_sum(values):
    ss = 0
    
    if isinstance(values, int):
        ss += values
    elif isinstance(values, str):
        ss += len(values)
    elif isinstance(values, dict):
        no_Dict = []
        no_Dict.extend(values.items()) 
        ss += calculate_structure_sum(no_Dict)
    elif len(values) != 1:
        for elem in values:
            ss += calculate_structure_sum(elem)
    else:
        ss += calculate_structure_sum(list(values)[0])
    return ss

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)

print(result)
