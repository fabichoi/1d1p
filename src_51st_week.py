# 51st week

# cofo 690 div3
# No. 1

'''
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        l = list(map(int,input().split(' ')))
        res = []
        sig = 1
        while len(l) > 0:
            res.append(l.pop(0) if sig == 1 else l.pop(-1))
            sig *= -1
        print(" ".join(map(str, res)))
'''

# No. 2
# 1920, 2019, 2020

'''
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        ar = input()
        answer = 'NO'
        if ar[0:2] == '20' and ar[-2:] == '20':
            answer = 'YES'
        if ar[0:1] == '2' and ar[-3:] == '020':
            answer = 'YES'
        if ar[0:3] == '202' and ar[-1:] == '0':
            answer = 'YES'
        if ar[0:4] == '2020' or ar[-4:] == '2020':
            answer = 'YES'
        print(answer)
'''

# No. 3
'''
if __name__ == "__main__":

    for _ in range(int(input())):
        n = int(input())

        if n > 45:
            print(-1)
            continue

        a = [0]
        res = []
        g = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        index = 0

        for i in range(11, 0, -1):
            for j in range(1, i-1):
                a.append(j)

        for i in range(1, len(g)):
            g[i] = g[i] + g[i-1]

        for i in range(len(g)):
            if n - g[i] <= 0:
                break
            index += 1
            res.append(a[g[index-1]])

        res.append(a[n])
        res.reverse()

        print(''.join(map(str,res)))

'''