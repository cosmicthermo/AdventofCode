
with open('data.txt', 'r') as f:
    data = [l.split() for l in f.readlines()]

# print(data)



def calibration(data):
    result = []
    for line in data:
        result.append(get_two_digit(line))
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
    lib1 = {'one':1, 'two':2, 'six':6}
    lib2 = {'four':4, 'five':5, 'nine':9}
    lib3 = {'three':3, 'seven':7, 'eight':8}
    digit, length = [], len(line)
    for i in range(length):
        if line[i].isdigit():
            digit.append(int(line[i]))
            continue
        if i + 3 <= length and (tmp:=line[i:i+3]) in lib1.keys():
            digit.append(lib1.get(tmp))
        if i + 4 <= length and (tmp:=line[i:i+4]) in lib2.keys():
            digit.append(lib2.get(tmp))
        if i + 5 <= length and (tmp:=line[i:i+5]) in lib3.keys():
            digit.append(lib3.get(tmp))
    return digit

print(calibration(data))