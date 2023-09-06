from collections import defaultdict

with open('data.txt', 'r') as f:
    commands = f.readlines()

# print(commands)

sizes = defaultdict(int)
stack = []

for temp in commands:
    if temp.startswith('$ ls') or temp.startswith('dir'):
        continue
    elif temp.startswith("$ cd"):
        c = temp.strip('\n').split(' ')
        # print(f'The striped c is {c}')
        if (name := c[2]) == '..':
            stack.pop()
        else:
            path = f'{stack[-1]}_{name}' if stack else name
            # print(path)
            stack.append(path)
    else:
        # a =temp.strip('\n').split(' ')
        size, file = temp.split()
        # print(size, file)
        ## Genius move
        for paths in stack:
            # print(paths)
            sizes[paths] += int(size)
            # print(sizes)


## Part 2
needed_size = 30000000 - (70000000 -sizes['/'])
sorted_sizes = defaultdict(int, sorted(sizes.items(), key=lambda x:x[1]))
print(sorted_sizes)
for cost in sorted_sizes.values():
    if cost > needed_size:
        print(cost)
        break
print(sum([s for s in sizes.values() if s < 100000])) ## part 1