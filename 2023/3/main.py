import itertools
with open('data.txt', 'r') as f:
    data = [r.strip() for r in f.readlines()]

# print(data, data[0][0])


def detect_legit_number(data):
    res = []
    n, m = len(data), len(data[0])
    direction = list(itertools.permutations([0, 1, -1], 2)) + [(1, 1), (-1, -1)]
    print(direction)
    for x in range(n):
        cur = 0
        while cur < m:
            for dx, dy in direction:
                nx, ny = x + dx, cur + dy
                if 0 <= nx < n and 0 <= ny < m and 0 <= cur < m and data[x][cur].isdigit() \
                    and not data[nx][ny].isdigit() and data[nx][ny] != '.':
                    pre = cur
                    while pre - 1 >= 0 and data[x][pre - 1].isdigit():
                        pre -= 1
                    while cur < m and data[x][cur].isdigit():
                        cur += 1
                    # print(x, pre, cur)
                    res.append(int(data[x][pre:cur]))
            cur += 1
        # print(res)
            

    return sum(res)

## Part One

# print(detect_legit_number(data))

## Part two
def detect_legit_ratio(data):
    res = []
    n, m = len(data), len(data[0])
    direction = list(itertools.permutations([0, 1, -1], 2)) + [(1, 1), (-1, -1)]
    for x in range(n):
        for y in range(m):
            if data[x][y] == '*':
                print(f'star is at {x} {y}')
                temp = set()
                for dx, dy in direction:
                    nx, ny = x + dx, dy+ y
                    if 0 <= nx < n and 0 <= ny < m and data[nx][ny].isdigit():
                        pre, cur = ny, ny
                        while pre - 1 >= 0 and data[nx][pre - 1].isdigit():
                            pre -= 1
                        while cur < m and data[nx][cur].isdigit():
                            cur += 1
                        temp.add((nx, pre, cur))
                print(temp)
                if len(temp) == 2:
                    current = [int(data[cx][pre:cur]) for cx, pre, cur in temp]
                    res.append(current[0]*current[1])
                    print(current)
    return sum(res)


print(detect_legit_ratio(data))