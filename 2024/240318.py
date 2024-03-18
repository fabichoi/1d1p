def question(nums, target):
    res = []

    def solve(nums, n):
        result = []
        l = len(nums)

        def whole_search(idx, comb):
            if len(comb) == n:
                result.append(comb.copy())
                return

            for i in range(idx, l):
                comb.append(nums[i])
                whole_search(i+1, comb)
                comb.pop()

        whole_search(0, [])
        return result

    for i in range(len(nums)):
        for n_list in solve(nums, i):
            if sum(n_list) == target:
                res.append(n_list)

    return res

print(question([1,2,3,4], 7))