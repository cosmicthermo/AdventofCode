
with open('data.txt', 'r') as f:
    data = [l.split() for l in f.readlines()]

# print(data)



def calibration(data, part_two):
    result = []
    for line in data:
        result.append(get_two_digit(line, part_two))
    return sum(result)

def get_two_digit(line, second_part=True):
    f, l =None, None
    assert len(line) != 0, f'Input line is zero.'
    if second_part:
        data = get_digit_out(line[0])
    print(data, line[0])
    for d in data:
        l = int(d)
        if f == None:
            f = int(d)
    
    res = f * 10 + l
    return res
## Part 1
# print(calibration(data))

## Part 2

def get_digit_out(line):
    lib = {'one':1, 'two':2, 'six':6, 'four':4, 'five':5, 'nine':9, 'three':3, 'seven':7, 'eight':8}
    digit, length = [], len(line)
    key_n = [3, 4, 5]
    for i in range(length):
        if line[i].isdigit():
            digit.append(int(line[i]))
            continue
        for n in key_n:
            if i + n <= length and (tmp:=line[i:i+n]) in lib.keys():
                digit.append(lib.get(tmp))
    return digit

print(calibration(data, part_two=True))