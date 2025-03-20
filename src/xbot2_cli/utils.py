import os
import yaml
import time

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

def as_list(value, check_none=True):
    if check_none and value is None:
        raise ValueError('Value cannot be None')
    if not check_none and value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]

def fetch_from_cache(cache_file: str, key: list[str]):
    if not os.path.exists(cache_file):
        return None
    cache_age = time.time() - os.path.getmtime(cache_file)
    if cache_age > 60:
        return None
    with open(cache_file, 'r') as f:
        cache = yaml.safe_load(f)
    return {k: cache[k] for k in key}

def write_to_cache(cache_file: str, data: dict):
    with open(cache_file, 'w') as f:
        yaml.dump(data, f)