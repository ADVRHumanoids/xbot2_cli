def print_table(table):
    table = list(table)
    longest_cols = [
        (max([len(str(row[i])) for row in table]) + 4)
        for i in range(len(table[0]))
    ]
    row_format = "".join(["{:<" + str(longest_col) + "}" for longest_col in longest_cols])
    for row in table:
        print(row_format.format(*row))
        
def pretty_cpp_types(type: str):
    type = type.replace('::__cxx11', '')
    if type.startswith('std::map'):
        tokens = type.split(',')
        type = f'{tokens[0]},{tokens[1]}>'
    elif type.startswith('std::vector'):
        type = type.split(',')[0] + '>'
    elif type.startswith('std::list'):
        type = type.split(',')[0] + '>'
    return type

def format_float(value: float, precision=2):
    # scientific notation
    if value == 0:
        return '0'
    if abs(value) < 10**-precision or abs(value) > 10**precision:
        return f'{value:.{precision}e}'
    # fixed point notation
    return f'{value:.{precision}f}'