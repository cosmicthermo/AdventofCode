
if __name__ == '__main__':
    a , x = 0, -1
    a += 1 if x > 0 else -1
    print(a)
    print(-4//4)
    lt = [0, 3]
    # print(lt+1)

    if (item:= 3 // 2) != 1:
        print(item)
    else:
        print(item+1)

    string = "lisi"
    dictionary = {}
    for s in string:
        dictionary[s] = dictionary.get(s, 0) + 1
    sorted_item = sorted(dictionary.items(), key=lambda x:x[1], reverse=True)
    values = [x[1] for x in sorted_item]
    data = list(range(26, 26-len(sorted_item), -1))
    print(sorted_item, values)
    print(data)
    print(values*data)