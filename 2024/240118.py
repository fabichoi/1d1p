def find_next_greater(numbers):
    n = len(numbers)
    result = [-1] * n
    stack = []
    for i in range(n):
        while stack and numbers[i] > numbers[stack[-1]]:
            result[stack.pop()] = numbers[i]
        stack.append(i)
    return result


if __name__ == '__main__':
    print(find_next_greater([4, 5, 2, 10, 8]))
