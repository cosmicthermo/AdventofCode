
def get_score(file):
    with open(file, 'r') as f:
        result = 0
        for item in f:
            strip_item = item.strip('\n')
            common_char = split_item(strip_item)
            result += score(common_char)

    return result


def split_item(item):
    first, second = item[:len(item)//2], item[len(item)//2:]
    for c in first:
        if c in second:
            return c
    return None


def score(common):
    if not common:
        return 0
    if common.isupper():
        return ord(common) - ord('A') + 27
    else:
        return ord(common) - ord('a') + 1

####################
## Part Two
####################

def get_score_group(file):
    with open(file, 'r') as f:
        data = f.read().strip('\n').split()
        # print(data)
        scores = [get_group_badge(data[x:(x+3)]) for x in range(0, len(data), 3)]
    return sum(scores)


def get_group_badge(badges):
    first, second = list(), list()
    result = None
    assert len(badges) == 3, f'Illegal badges length {len(badges)}'
    for c1 in badges[0]:
        if c1 in badges[1]:
            first.append(c1)
        if c1 in badges[-1]:
            second.append(c1)
    for c2 in first:
        if c2 in second:
            result = c2
            break
    final_score = score(result)
    return final_score


if __name__ == '__main__':
    test_file = 'data.txt'
    print(get_score_group(test_file))
    