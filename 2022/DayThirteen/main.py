with open('test.txt', 'r') as f:
    grid = [row.split for row in f.readlines()]
    