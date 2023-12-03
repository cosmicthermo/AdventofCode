from collections import deque
DIVISOR = 1

class Monkey_buiness_test:
    def __init__(self):
        self.monkey_item = [deque() for _ in range(4)]
        self.initialize_deque()
        self.monkey_one, self.monkey_two, self.monkey_three, self.monkey_four = 0, 0, 0,0

    def initialize_deque(self):
        start_list = [[79, 98], [54, 65, 75, 74], [79, 60, 97], [74]]
        for i, ele in enumerate(start_list):
            for item in ele:
                self.monkey_item[i].append(item)
            # print(self.monkey_item[i])
            # print(i)

    def one_round(self):
        for idx, monkey in enumerate(self.monkey_item):
            while monkey:
                if idx == 0:
                    self.monkey_one += 1
                    pop_item = monkey.popleft()
                    pop_item *= 19
                    if (append_item:=pop_item) % 23 == 0:
                        self.monkey_item[2].append(append_item)
                    else:
                        self.monkey_item[3].append(append_item)
                    # print(append_item)
                elif idx == 1:
                    self.monkey_two += 1
                    pop_item = monkey.popleft()
                    # print(pop_item)
                    pop_item += 6
                    if (append_item:=pop_item) % 19 == 0:
                        self.monkey_item[2].append(append_item)
                    else:
                        self.monkey_item[0].append(append_item)
                    # print(append_item)
                elif idx == 2:
                    self.monkey_three += 1
                    pop_item = monkey.popleft()
                    # print(pop_item)
                    pop_item = pop_item ** 2
                    if (append_item:=pop_item) % 13 == 0:
                        self.monkey_item[1].append(append_item)
                    else:
                        self.monkey_item[3].append(append_item)
                    # print(append_item)
                elif idx == 3:
                    self.monkey_four += 1
                    pop_item = monkey.popleft()
                    # print(pop_item)
                    pop_item += 3
                    if (append_item:=pop_item) % 17 == 0:
                        self.monkey_item[0].append(append_item)
                    else:
                        self.monkey_item[1].append(append_item)
                    # print(append_item)
        # print(self.monkey_item)

    def print_monkeyaccess(self):
        monkey_access = [self.monkey_one, self.monkey_two, self.monkey_three, self.monkey_four]
        for idx, item in enumerate(monkey_access):
            print(f'Monkey {idx} inspected items {item} times')
        monkey_access.sort(reverse=True)
        print(monkey_access)
        print(f'The monkey business is total of {monkey_access[0] * monkey_access[1]}')
        
#######
## Part One
#######
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor

class Monkey_buiness_part_one:
    def __init__(self):
        self.monkey_item = [deque() for _ in range(8)]
        self.initialize_deque()
        self.monkey_access = [0] * 8
        self.operations = [
            (lambda x: x*2, [6, 1], 5),
            (lambda x: x*13, [2, 6], 2),
            (lambda x: x+5, [7, 5], 19),
            (lambda x: x+6, [0, 4], 7),
            (lambda x: x+1, [0, 1], 17),
            (lambda x: x+4, [4, 3], 13),
            (lambda x: x+2, [2, 7], 3),
            (lambda x: x**2, [3, 5], 11)
        ]

    def initialize_deque(self):
        start_list = [[98, 89, 52], [57, 95, 80, 92, 57, 78], [82, 74, 97, 75, 51, 92, 83], [97, 88, 51, 68, 76], [63], [94, 91, 51, 63], [61, 54, 94, 71, 74, 68, 98, 83], [90, 56]]
        for i, ele in enumerate(start_list):
            for item in ele:
                self.monkey_item[i].append(item)
            # print(self.monkey_item[i])
            # print(i)
    
    def run_one_round(self):
        for idx, monkey in enumerate(self.monkey_item):
            while monkey:
                self.monkey_access[idx] += 1
                operation, destinations, condition = self.operations[idx]
                pop_item = operation(monkey.popleft())
                append_item = pop_item // DIVISOR
                dest_idx = destinations[0] if append_item % condition == 0 else destinations[1]
                self.monkey_item[dest_idx].append(append_item)
        print(self.monkey_item)

    def process_monkey(self, idx):
        monkey = self.monkey_item[idx]
        new_items = []
        while monkey:
            self.monkey_access[idx] += 1
            operation, destinations, condition = self.operations[idx]
            pop_item = operation(monkey.popleft())
            append_item = pop_item // DIVISOR
            dest_idx = destinations[0] if append_item % condition == 0 else destinations[1]
            new_items.append((dest_idx, append_item))
        return new_items

    def run_one_round_parallel(self):
        with ThreadPoolExecutor() as executor:
            results = list(executor.map(self.process_monkey, range(8)))

        for idx, new_items in enumerate(results):
            for dest_idx, append_item in new_items:
                self.monkey_item[dest_idx].append(append_item)


    def run_round(self, round):
        for _ in range(round):
            self.run_one_round()

    def print_monkeyaccess(self):
        monkey_access = self.monkey_access.copy()
        for idx, item in enumerate(monkey_access):
            print(f'Monkey {idx} inspected items {item} times')
        monkey_access.sort(reverse=True)
        print(monkey_access)
        # print(self.monkey_item)
        print(f'The monkey business is total of {monkey_access[0] * monkey_access[1]}')

#######
## Part Two
## Help
# Chinese Remainder Theorem https://crypto.stanford.edu/pbc/notes/numbertheory/crt.html
# the modulo of coprime has the same modulo under each of the prime
# What I meant is 
# a, b, c.. k is the prime divisor, given some x, x ≡ a1 (mod a), x ≡ a2 (mod b)...
# if x ≡ y (mod a*b*c...*k), then y ≡ a1 (mod a), y ≡ a2 (mod b) holds for all divisors
#######
import math
class MonkeyBuinessBase:
    def __init__(self, monkey_count, my_operations, data):
        self.monkey_item = [deque() for _ in range(monkey_count)]
        self.monkey_access = [0] * monkey_count
        self.operations = my_operations
        self.initialize_deque(data)
        self.divisor = self.multiply_divisor(my_operations)
    
    def multiply_divisor(self, operations):
        factor = [x[-1] for x in operations]
        # print(factor, math.prod(factor))
        return math.prod(factor)

    def initialize_deque(self, data):
        assert len(data) == len(self.monkey_item), f'Data has different len with monkey_item'
        for i, ele in enumerate(data):
            self.monkey_item[i].extend(ele)
        print(self.monkey_item)

    def run_one_round(self):
        for idx, monkey in enumerate(self.monkey_item):
            while monkey:
                self.monkey_access[idx] += 1
                operation, destinations, condition = self.operations[idx]
                pop_item = operation(monkey.popleft())
                append_item = pop_item % self.divisor
                dest_idx = destinations[0] if append_item % condition == 0 else destinations[1]
                self.monkey_item[dest_idx].append(append_item)
        # print(self.monkey_item)

    def run_round(self, round):
        for _ in range(round):
            self.run_one_round()

    def print_monkeyaccess(self):
        monkey_access = self.monkey_access.copy()
        for idx, item in enumerate(monkey_access):
            print(f'Monkey {idx} inspected items {item} times')
        monkey_access.sort(reverse=True)
        print(monkey_access)
        # print(self.monkey_item)
        print(f'The monkey business is total of {monkey_access[0] * monkey_access[1]}')


class MonkeyBizPartTwo(MonkeyBuinessBase):
    def __init__(self):
        super().__init__(8, 
                         [
                            (lambda x: x*2, [6, 1], 5),
                            (lambda x: x*13, [2, 6], 2),
                            (lambda x: x+5, [7, 5], 19),
                            (lambda x: x+6, [0, 4], 7),
                            (lambda x: x+1, [0, 1], 17),
                            (lambda x: x+4, [4, 3], 13),
                            (lambda x: x+2, [2, 7], 3),
                            (lambda x: x**2, [3, 5], 11)
                        ], 
                         [[98, 89, 52], [57, 95, 80, 92, 57, 78], [82, 74, 97, 75, 51, 92, 83], [97, 88, 51, 68, 76], [63], [94, 91, 51, 63], [61, 54, 94, 71, 74, 68, 98, 83], [90, 56]])
    
class MonkeyBizTest(MonkeyBuinessBase):
    def __init__(self):
        super().__init__(4, 
                         [
                            (lambda x: x*19, [2, 3], 23),
                            (lambda x: x+6, [2, 0], 19),
                            (lambda x: x**2, [1, 3], 13),
                            (lambda x: x+3, [0, 1], 17)
                        ], 
                        [[79, 98], [54, 65, 75, 74], [79, 60, 97], [74]]
                        )



if __name__ == '__main__':
    ## Part Two
    import time
    start_time = time.time()
    monkey = MonkeyBizPartTwo()
    print(monkey.divisor)
    round = 10000
    monkey.run_round(round)
    end_time = time.time()
    monkey.print_monkeyaccess()
    elapsed_time = end_time - start_time
    print(f"Time taken: {elapsed_time} seconds for {round}")

    # import time
    # start_time = time.time()
    # monkey = Monkey_buiness_test()
    # for _ in range(1000):
    #     monkey.one_round()
    # end_time = time.time()
    # monkey.print_monkeyaccess()
    # elapsed_time = end_time - start_time
    # print(f"Time taken: {elapsed_time} seconds")


    ## Part one
    # import time
    # start_time = time.time()
    # monkey = Monkey_buiness_part_one()
    # round = 2
    # monkey.run_round(round)
    # end_time = time.time()
    # monkey.print_monkeyaccess()
    # elapsed_time = end_time - start_time
    # print(f"Time taken: {elapsed_time} seconds for {round}")
