## function for updating the indexes
# def update_board(H, T, dir):
filename = 'test.txt'
with open(filename, 'r') as f:
    data = f.readlines()
    # print(data)
    ## The first step is to initialize the H, T point
H, T = [0,0], [0,0]
## Step Two
# NUMBER = 10
# snake = [[0,0] for _ in range(NUMBER)]
record = set()

for i in data:
    tmp = i.strip('\n').split()
    dir, step = tmp[0], tmp[-1]
    # print('--------')
    # print(dir, step)
    for _ in range(int(step)):
        if dir == 'R':
            H[0] += 1
        elif dir == 'L':
            H[0] -= 1
        elif dir == 'U':
            H[1] += 1
        elif dir == 'D':
            H[1] -= 1
        ## Check the rule of closeness
        x, y = (H[0]-T[0]), (H[1]-T[1])
        distance = abs(abs(x) - abs(y))
        if distance >= 2:
            if y == 0:
                T[0] += 1 if x > 0 else -1
            elif x == 0:
                T[1] += 1 if y > 0 else -1
        elif distance >= 1 and x != 0 and y != 0:
            T[0] += x // abs(x)
            T[1] += y // abs(y)
        # print(H, T)
        # ### Step One
        # record.add(tuple(T.copy()))
        # print()
            # print(snake[i],snake[i+1])
        # record.add(tuple(snake[-1].copy()))
    

# dir, step = 'R', 4

## Debug: implement a board for visualization

## Step Two
def step_two():
    filename = 'data.txt'
    with open(filename, 'r') as f:
        data = f.readlines()
        print(data)
    
    ## Initialize Snake
    snake = [[0,0] for _ in range(10)]
    record = set()
    for i in data:
        tmp = i.strip('\n').split()
        dir, step = tmp[0], tmp[-1]
        update_snake(snake, dir, step, record)
    print(record)
    print(len(record))

def update_snake(snake, dir, step, record):
    for idx in range(int(step)):
        ## The Snake head is move by instruction
        if dir == 'R':
            snake[0][0] += 1
        elif dir == 'L':
            snake[0][0] -= 1
        elif dir == 'U':
            snake[0][1] += 1
        elif dir == 'D':
            snake[0][1] -= 1
        ## update the rest of the body
        for i in range(9):
            x, y = (snake[i][0]-snake[i+1][0]), (snake[i][1]-snake[i+1][1])
            distance = abs(abs(x) - abs(y))
            if distance >= 2:
                if y == 0:
                    snake[i+1][0] += 1 if x > 0 else -1
                elif x == 0:
                    snake[i+1][1] += 1 if y > 0 else -1
            elif distance >= 1 and x != 0 and y != 0:
                snake[i+1][0] += x // abs(x)
                snake[i+1][1] += y // abs(y)
            elif distance == 0 and abs(x) >= 2:
                snake[i+1][0] += x // abs(x)
                snake[i+1][1] += y // abs(y)
        record.add(tuple(snake[-1]))
        ## Display the updated snake
        # print(f'{dir} - {step} {idx+1}th')
        # for i in snake:
        #     print(i)
        # print()
        
    
if __name__ == '__main__':
    # print(f'Hello')
    step_two()
