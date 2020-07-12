import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 4 + 7


def resolve():
    n = int(input())
    s = input()

    dp = [[0] * (1 << 3) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(1, n + 1):
        mask = 2 if s[i - 1] == "J" else 1 if s[i - 1] == "O" else 0
        for S_now in range(1 << 3):
            if i == 1:
                if S_now & (1 << 2) and S_now & (1 << mask):
                    dp[i][S_now] = 1
            else:
                if S_now & (1 << mask):
                    for S_prev in range(1 << 3):
                        if S_now & S_prev:
                            dp[i][S_now] += dp[i - 1][S_prev]
                            dp[i][S_now] %= mod
    print(sum(dp[-1]) % mod)


if __name__ == '__main__':
    resolve()
