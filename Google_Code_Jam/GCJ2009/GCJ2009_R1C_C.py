# https://codingcompetitions.withgoogle.com/codejam/round/0000000000433247/0000000000432cc6
# Bribe the Prisoners
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    for t in range(n):
        p, q = map(int, input().split())
        A = [0] + list(map(int, input().split())) + [p + 1]

        dp = [[f_inf] * (q + 2) for _ in range(q + 1)]
        for i in range(q + 1):
            dp[i][i + 1] = 0

        for length in range(2, q + 2):
            l = 0
            r = l + length
            while r < q + 2:
                min_cost = f_inf
                for m in range(l + 1, r):
                    min_cost = min(min_cost, dp[l][m] + dp[m][r])
                dp[l][r] = min_cost + A[r] - A[l] - 2
                l += 1
                r += 1

        res = dp[0][q + 1]
        print("Case #{}: {}".format(t + 1, res))


if __name__ == '__main__':
    resolve()
