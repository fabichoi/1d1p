r, b = map(int, input().split(' '))
w = 0
for l in range(1, b+1):
    if b % l != 0:
        continue    
    w = b // l
    sum = w * 2 + l * 2 + 4
    if sum == r:
        if w > l:
            print(str(w + 2) + " " + str(l + 2))
        else:
            print(str(l + 2) + " " + str(w + 2))
        break