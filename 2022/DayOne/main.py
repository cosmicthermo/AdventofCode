
def max_energy(file_name):
    result = 0
    val = 0
    with open(file_name) as file:
        for item in file:
            if item == '\n':
                result = max(result, val)
                val = 0
            else:
                val += int(item)
    return result
            



if __name__ == '__main__':
    file_name = 'data.txt'
    print(max_energy(file_name=file_name))
    