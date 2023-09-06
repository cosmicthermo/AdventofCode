SIZE_LIMIT = 100000

class TreeNode:
    def __init__(self, name, val=0, label=""):
        self.name = name
        self.val = val if val < 100000 else 0
        self.label = label
        self.next = []

def count_sizes_file(filename):
    total = 0
    with open(filename, 'r') as f:
        for item in f:
            if item[0].isdigit():
                digit = int(item.split(" ")[0])
                # print(digit)
                if digit < SIZE_LIMIT:
                    print(digit)
                    total += digit
                    # print(total)
    return total

def parse_file(filename):
    root = TreeNode('/', label='dir')
    stack = [root]
    with open(filename, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            # print(line)
            if line.startswith("$ cd "):
                path = line.split(" ")[2:]
                if path[0] == '..':
                    stack.pop()
                elif path[0] == '/':
                    stack = [root]
                else:
                    current = next(node for node in stack[-1].next if node.name == path[0])
                    stack.append(current)
            elif line.startswith("$ ls"):
                continue
            else:
                parts = line.split()
                if parts[0] == 'dir':
                    new_dir = TreeNode(parts[1],label='dir')
                    stack[-1].next.append(new_dir)
                else:
                    stack[-1].next.append(TreeNode(parts[1], val=int(parts[0])))
                    # print(parts[0])
                    # print_tree(stack[-1])
    return root

def update_tree(node):
    for child in node.next:
        update_tree(child)
        node.val += child.val

def print_tree(node, indent=""):
    print(node.name + " " + node.label + " " + str(node.val))
    for child in node.next:
        print_tree(child, indent + " ")

class UpdateValues:
    def __init__(self) -> None:
        self.values = []

    def append_value(self, node):
        for child in node.next:
            if child.label == 'dir' and child.val < SIZE_LIMIT:
                self.values.append(child.val)
            self.append_value(child)
            

    def calculate_final_values(self):
        print(self.values)
        print(f'The sum of the values list is {sum(self.values)}')


if __name__ == '__main__':
    # count_sizes_file('test.txt')
    root = parse_file('test.txt')
    update_tree(root)
    # root.val = 0
    # print_tree(root)
    # print('\n\n')
    # calculate_value(root)
    print_tree(root)
    value = UpdateValues()
    value.append_value(root)
    value.calculate_final_values()
    ## Still too high 3403473
