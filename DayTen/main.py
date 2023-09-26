def part_one():
    filename = 'data.txt'
    with open(filename, 'r') as f:
        data = f.readlines()
    register, count = [], []

    for item in data:
        tmp = item.strip('\n').split()
        if tmp[0] == 'addx':
            register.append(int(tmp[-1]))
            count.append(2)
        elif tmp[0] == 'noop':
            register.append(0)
            count.append(1)
    # print(register)
    # print(count)
    ## Part One
    cycle = [20, 60, 100, 140, 180, 220]
    total = 0
    # for cy in cycle:
    #     total += cumsum(cy, count, register)* cy
    #     print(f'The {cy} cycle of cpu register count is {cumsum(cy, count, register)}, signal strength is {cumsum(cy, count, register)* cy}')
    # print(total)

    ## Part Two
    # 
    crt = ""
    # for idx in range(len(crt)):
    pointer = 0
    spike = [0, 2]
    while len(crt) < 240:
        for _ in range(count[pointer]):
            # print(f'At position {len(crt)} draw')
            if len(crt) == 240:
                break
            position = len(crt) % 40
            if spike[0] <= position <= spike[1]:
                crt += '#'
            else:
                crt += '.'
            # print(crt)
        spike[0] += register[pointer]
        spike[1] += register[pointer]
        pointer += 1
    
    for i in range(0, 201, 40):
        print(crt[i:(i+40)])

        

    
def cumsum(cycle, count, register):
    pointer = 0
    for idx, item in enumerate(count):
        pointer += item
        if pointer == cycle:
            # print(register[:idx+1])
            return sum(register[:idx]) + 1
        elif pointer > cycle:
            # print(pointer)
            return sum(register[:idx]) + 1

                

if __name__ == '__main__':
    part_one()