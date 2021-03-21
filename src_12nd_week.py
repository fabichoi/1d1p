# problem A
'''
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split(' ')))

    cnt = 0
    for i in range(len(a)-1):
        max_a = max(a[i],a[i+1])
        min_a = min(a[i],a[i+1])
        next_a = min_a * 2
        while True:
            if next_a < max_a:
                next_a *= 2
                cnt += 1
            else:
                break
    print(cnt)
'''

# problem B

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split(' ')))

    need_to_be = len(a) // 3
    cnt = 0
    ar = [0, 0, 0]

    for aa in a:
        ar[aa % 3] += 1


    for i in range(2):
        if ar[i] > need_to_be:
            cnt += ar[i] - need_to_be
            ar[i+1] += ar[i] - need_to_be
            ar[i % 3] = need_to_be

    for i in range(1,3):
        if ar[i] > need_to_be:
            cnt += ar[i] - need_to_be
            ar[(i+1)%3] += ar[i] - need_to_be
            ar[i%3] = need_to_be

    for i in range(2,4):
        if ar[i%3] > need_to_be:
            cnt += ar[i%3] - need_to_be
            ar[(i+1)%3] += ar[i%3] - need_to_be
            ar[i%3] = need_to_be

    print(cnt)



