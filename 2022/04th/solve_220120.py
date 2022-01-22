# BOJ 1145
from itertools import combinations
from math import gcd


def get_min(arr):
    first_lcm = (arr[0] * arr[1] // gcd(arr[0], arr[1]))
    return (first_lcm * arr[2]) // gcd(first_lcm, arr[2])


l = list(map(int, input().split(' ')))
n = 3
ar = list(combinations([0, 1, 2, 3, 4], n))
result = 9876543210
for a in range(len(ar)):
    min_value = get_min([l[ar[a][0]], l[ar[a][1]], l[ar[a][2]]])
    if result > min_value:
        result = min_value
print(result)