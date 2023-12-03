from heapq import heappush, heappop

with open('data.txt', 'r') as f:
    grid = [row.strip() for row in f.readlines()]

# print(grid)
def get_neighbors(row, col):
    h = get_height(row, col)
    neighbors = []
    directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
    for x, y in directions:
        nx, ny = row+x, col+y
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and get_height(nx, ny) - h <= 1:
            neighbors.append((nx, ny))
    return neighbors


def get_height(row, col):
    if grid[row][col] == 'S':
        return 0
    if grid[row][col] == 'E':
        return 25
    return ord(grid[row][col]) - 97

def shortest_step(start, end):
    visited = set()
    queue = []
    heappush(queue, (0, start))

    while queue:

        steps, node = heappop(queue)
        if node not in visited:
            visited.add(node)
            if node == end:
                return steps
            for dx, dy in get_neighbors(node[0], node[1]):
                heappush(queue, (steps+1, (dx, dy)))

    return -1

def find_s_e(grid):
    s, e = None, None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # print(grid[i][j])
            if grid[i][j] == 'S':
                s = (i, j)
            if grid[i][j] == 'E':
                e = (i, j)
    return s, e if (s != None and e != None) else None
s, e = find_s_e(grid)
print(shortest_step(s, e))

## Part two
shortest_path = float('inf')
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'a':
            tmp = shortest_step((i, j), e)
            shortest_path = min(shortest_path, tmp if tmp > -1 else float('inf'))
print(shortest_path)


"""
Inspiration from https://github.com/silentw0lf/advent_of_code_2022/blob/main/12/solve.py
"""