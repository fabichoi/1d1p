# TopCoder : FriendScore

class FriendScore:

    def highestScore(self, friends):
        ans = 0
        n = len(friends[0])

        for i in range(n):
            cnt = 0
            for j in range(n):
                if i == j:
                    continue

                if friends[i][j] == 'Y':
                    cnt += 1
                else:
                    for k in range(n):
                        if friends[j][k] == 'Y' and friends[k][i] == 'Y':
                            cnt += 1
                            break
            ans = max(ans, cnt)

        return ans