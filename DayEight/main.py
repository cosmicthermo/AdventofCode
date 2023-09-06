with open('data.txt', 'r') as f:
    data = f.readlines()
col, row = len(data[0].split()[0]), len(data)
well = [[0]*col for _ in range(row)]

for c in range(col):
    for r in range(row):
        if data[r][c] == '\n':
            continue
        # print(data[r][c])
        well[r][c] = int(data[r][c])
print(well)


def is_visible(well, r, c):
    row, col = len(well), len(well[0])
    # Up
    if r > 0 and well[r-1][c] < well[r][c]:
        i = r
        while i > 0 and well[i-1][c] < well[r][c]:
            if i-1 == 0:
                return True
            i -= 1
    # Down
    if r < row-1 and well[r+1][c] < well[r][c]:
        i = r
        while i < row-1 and well[i+1][c] < well[r][c]:
            if i+1 == row-1:
                return True
            i += 1
    # Right
    if c < col-1 and well[r][c+1] < well[r][c]:
        j = c
        while j < col-1 and well[r][j+1] < well[r][c]:
            if j+1 == col-1:
                return True
            j += 1
    # Left 
    if c > 0 and well[r][c-1] < well[r][c]:
        j = c
        while j > 0 and well[r][j-1] < well[r][c]:
            if j-1 == 0:
                return True
            j -= 1
    return False

count = 2 * (col + row) - 4
for i in range(1, row-1):
    for j in range(1, col-1):
        # print(f'Location is {(i, j)}, value {well[i][j]}')
        if (is_visible(well,i,j)):
            count += 1
    # print()
print(count)

# Part 2
def visiblilty_score(well, r, c):
    row, col = len(well), len(well[0])
    up, dw, lf, rt = 1, 1, 1, 1
    # Up
    if r > 0 and well[r-1][c] < well[r][c]:
        i = r
        while i > 0 and well[i-1][c] < well[r][c]:
            up += 1
            i -= 1
        if i > 0 and well[i-1][c] >= well[r][c]:
            up += 1
    # Down
    if r < row-1 and well[r+1][c] < well[r][c]:
        i = r
        while i < row-1 and well[i+1][c] < well[r][c]:
            dw += 1
            i += 1
        if i < row-1 and well[i+1][c] >= well[r][c]:
            dw += 1
    # Right
    if c < col-1 and well[r][c+1] < well[r][c]:
        j = c
        while j < col-1 and well[r][j+1] < well[r][c]:
            rt += 1
            j += 1
        if j < col-1 and well[r][j+1] >= well[r][c]:
            rt += 1
    # Left 
    if c > 0 and well[r][c-1] < well[r][c]:
        j = c
        while j > 0 and well[r][j-1] < well[r][c]:
            lf += 1
            j -= 1
        if j > 0 and well[r][j-1] >= well[r][c]:
            lf += 1
    up = up - 1 if up > 1 else 1
    dw = dw - 1 if dw > 1 else 1
    lf = lf - 1 if lf > 1 else 1
    rt = rt - 1 if rt > 1 else 1
    # print(f'up {up},left {lf} , right {rt}, down {dw}')
    return up * dw * lf * rt

score = 0
for i in range(1, row-1):
    for j in range(1, col-1):
        score = max(score, visiblilty_score(well,i,j))

print(score)
# print(visiblilty_score(well,1,2))