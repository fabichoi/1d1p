'''
# boj 16968
if __name__ == "__main__":
    n = input()
    l = {'c':26, 'd':10}
    res = 1
    before = ''
    for i in range(len(n)):
        if n[i] == before:
            res *= (l.get(n[i])-1)
        else:
            res *= l.get(n[i])

        before = n[i]
    print(res)
'''


# boj 14681
if __name__ == "__main__":
    x = int(input())
    y = int(input())
    answer = 0
    if x > 0 and y > 0:
        answer = 1
    if x > 0 and y < 0:
        answer = 4
    if x < 0 and y < 0:
        answer = 3
    if x < 0 and y > 0:
        answer = 2
    print(answer)