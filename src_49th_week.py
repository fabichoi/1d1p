# 49th week

'''
class boj15953:

    def solve(self, a, b):
        price_2017 = [0,
                      500,
                      300, 300,
                      200, 200, 200,
                      50, 50, 50, 50,
                      30, 30, 30, 30, 30,
                      10, 10, 10, 10, 10, 10]
        price_2018 = [0,
                      512,
                      256, 256,
                      128, 128, 128, 128,
                      64, 64, 64, 64, 64, 64, 64, 64,
                      32, 32, 32, 32, 32, 32, 32, 32,
                      32, 32, 32, 32, 32, 32, 32, 32]

        if a >= len(price_2017):
            a = 0
        if b >= len(price_2018):
            b = 0

        return (price_2017[a] + price_2018[b]) * 10000

if __name__ == "__main__":
    for _ in range(int(input())):
        a, b = map(int, input().split(' '))
        print(boj15953.solve(_, a, b))
'''

class boj2851:

    def solve(ar):
        n = len(ar)
        res = set()
        for i in range(n):
            t = ar[i]
            for j in range(i+1,n):
                t += ar[j]
                if t > 100:
                    res.add(t)
                    res.adD(t-ar[j])
                if t == 100:
                    return 100
        if len(res) == 0:
            return t
        print(res)
        return res


'''
if __name__ == "__main__":
    print(boj2851.solve([1,2]))
'''