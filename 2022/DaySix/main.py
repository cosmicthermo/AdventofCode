DISTINCT_CHAR = 14

def get_index(example):
    first, second = 0, 1
    while second < len(example):
        if first == second:
            second += 1
        while example[second] not in example[first:second]:
            if second - first + 1 == DISTINCT_CHAR:
                return second + 1
            second += 1
        for i in range(first, second):
            if example[i] == example[second]:
                first = i + 1
                break
    
if __name__ == '__main__':
    test1 = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
    with open('data.txt', 'r') as f:
        for item in f:
            # print(item)
            print(get_index(item))
