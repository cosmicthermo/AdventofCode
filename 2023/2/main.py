with open('data.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]

# print(data)

def sum_id(data, two):
    res = 0
    for line in data:
        res += get_legit_id(line, two)
    return res

def get_legit_id(line, part_two):
    assert type(line) != str(), f'Datatype should be string'
    rules = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }
    bag = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }
    id, rest = int(line.split(':')[0].split()[-1]), line.split(':')[-1]
    for batch in rest.split(';'):
        for data in batch.split(','):
            numb, color = data.split()
            if part_two:
                if color in bag:
                    bag[color] = max(int(numb), bag.get(color))
            else:
                if rules.get(color, float('inf')) < int(numb):
                    return 0
    
    result = list(accum_mul(bag.values()))[-1]

    return result if part_two else id

def accum_mul(values):
    it = iter(values)
    initial = next(it)
    total = initial
    yield total
    for element in it:
        total *= element
        yield total

# print(list(accum_mul([2,3,4])))
## Part One
print(sum_id(data, False))

# Part Two

print(sum_id(data, True))
