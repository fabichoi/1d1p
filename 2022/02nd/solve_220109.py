# BOJ 1049
n, m = map(int, input().split(' '))
min_set_price, min_piece_price = 1000, 1000
for _ in range(m):
    set_price, piece_price = map(int, input().split(' '))
    min_set_price = min_set_price if min_set_price < set_price else set_price
    min_piece_price = min_piece_price if min_piece_price < piece_price else piece_price
nn = ((n // 6) + (1 if n % 6 != 0 else 0)) * 6
min_ar = [0 for _ in range(nn + 1)]
min_ar[1] = min_piece_price
for i in range(2, nn + 1):
    if i % 6 != 0:
        min_ar[i] = min_ar[i - 1] + min_piece_price
        continue
    min_ar[i] = min(min_ar[i - 1] + min_piece_price, min_ar[i - 6] + min_set_price)
print(min(min_ar[n], min_ar[nn]))
