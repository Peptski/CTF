def solve(num):
    queue = [[num, []]]
    chars = [i for i in range(97, 123)]

    possible = []

    while queue:
        number = queue.pop()
        if number[0] == 1: 
            str = [chr(val) for val in number[1]]
            sortString = sorted(str)
            if not sortString in possible: possible.append(sortString)
        else:
            for i in chars:
                if (number[0] / i) % 1 == 0:
                    if len(number[1]) < 10:
                        queue.append([int(number[0]/i), number[1] + [i]])
    return possible

print(solve(19811137522176000))