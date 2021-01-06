# Codeforces Round  693 (Div. 3)
# No.1

'''
if __name__ == "__main__":
    for _ in range(int(input())):
        res = 1
        w, h, n = map(int, input().split(' '))
        while True:
            if w % 2:
                break
            w //= 2
            res *= 2
        while True:
            if h % 2:
                break
            h //= 2
            res *= 2
        print("YES" if res >= n else "NO")
'''

# No.2

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int,input().split(' ')))
        if (a.count(1) % 2) or (a.count(2) % 2):
            print("NO")
        else:
            print("YES")




