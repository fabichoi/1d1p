
# n개의 조합을 구하자
# 입력은 list, int
# 출력은 list

input_list = [1,2,3,4]
n = 2
res = []
l = len(input_list)

# 나올수 있는 값은
# [1,2,3], [1,2,4], [1,3,4], [2,3,4]
# 1을 고른다음 순회, 2를 고르고 순회, 3을 고르고 순회

def solve(idx, comb):
    if len(comb) == n:
        return res.append(comb.copy())

    for i in range(idx, l):
        comb.append(input_list[i])
        solve(i + 1, comb)
        comb.pop()


if __name__ == '__main__':
    solve(0, [])
    print(res)

