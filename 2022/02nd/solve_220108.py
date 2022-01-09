# BOJ 1032
filenames = [input() for _ in range(int(input()))]
result = list(filenames[0])
for i in range(1, len(filenames)):
    for j in range(len(result)):
        result[j] = result[j] if filenames[i][j] == result[j] else '?'
print(''.join(result))
