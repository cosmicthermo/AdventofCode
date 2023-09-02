
def get_all_pair(file):
    with open(file, 'r') as f:
        amount = 0
        i = 10
        for item in f:
            amount += strip_pair(item)
            # i -= 1
            # if i<0:
            #     break
    return amount

def strip_pair(item):
    pair = item.strip('\n').split(',')
    assert len(pair) == 2, f'Length of the pair is not 2, is {len(pair)}'
    ft, sd = pair[0].split('-'), pair[-1].split('-')
    d1, d2, d3, d4 = int(ft[0]), int(ft[1]), int(sd[0]), int(sd[1])

    return overlapping(d1, d2, d3, d4)

def inclusiveness(d1, d2, d3, d4):
    if d3 <= d1 <= d4 and d3 <= d2 <= d4:
        return 1
    if d1 <= d3 <= d2 and d1 <= d4 <= d2:
        return 1
    return 0

def overlapping(d1, d2, d3, d4):
    if d3 <= d1 <= d4 or d3 <= d2 <= d4:
        return 1
    if d1 <= d3 <= d2 or d1 <= d4 <= d2:
        return 1
    return 0


if __name__ == '__main__':
    file_name = 'data.txt'
    print(get_all_pair(file_name))

