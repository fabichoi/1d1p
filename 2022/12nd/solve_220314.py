# BOJ 1668
trophies = []
left_max, right_max = 0, 0
left_answer, right_answer = 0, 0
n = int(input())
for _ in range(n):
    trophies.append(int(input()))
left_answer = 0
for i in range(n):
    if left_max < trophies[i]:
        left_max = trophies[i]
        left_answer += 1
right_answer = 0
for i in range(n-1, -1, -1):
    if right_max < trophies[i]:
        right_max = trophies[i]
        right_answer += 1

print(left_answer)
print(right_answer)
