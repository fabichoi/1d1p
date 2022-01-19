# BOJ 1110
init_num = int(input())
res = 0
num = init_num

while True:
    a = num // 10
    b = num % 10
    c = (a + b) % 10
    num = (b * 10) + c
    res += 1
    if init_num == num:
        break

print(res)
