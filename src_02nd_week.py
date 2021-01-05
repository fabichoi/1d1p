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
        a = sorted(list(map(int,input().split(' '))))
        while len(a) > 2:
            first = a.pop()
            second = a.pop()
            if first != second:
                a.append(first)

        if len(a) == 1:
            print("NO")
        else:
            if(a[0] == a[1]):
                print("YES")
            else:
                print("NO")




