from collections import deque
# def get_initialization_setup()

def game_setup(filename, setup_line):
    with open(filename, 'r') as f:        
        x = f.readline().replace(' ', '*')
        group_stack = [deque() for _ in range(len(x)//4)]

    with open(filename, 'r') as file:
        position = setup_line
        while position > 0:
            x = file.readline().replace(' ', '*')
            for i in range(0, len(x), 4):
                if x[i] == '*':
                    continue
                numb_stack = i // 4
                group_stack[numb_stack].append(x[i+1])
            position -= 1
        print(group_stack)

        print(file.readline())
        for item in file:
            instruction = item.strip('\n').split(' ')
            block, initial, final = instruction[1], instruction[-3], instruction[-1]
            move_block(instruction, group_stack)
        print(group_stack)
        res = ""
        for queue in group_stack:
            res += queue.popleft()
        return res

def move_block(instruction, group_stack):
    block, initial, final = int(instruction[1]), int(instruction[-3]), int(instruction[-1])
    temp = []
    while block > 0:
        item = group_stack[initial-1].popleft()
        temp.append(item)
        block -= 1
    while temp:
        temp_item = temp.pop()
        group_stack[final-1].appendleft(temp_item)



if __name__ == '__main__':
    filename = 'data.txt'
    print(game_setup(filename, 9))
        
