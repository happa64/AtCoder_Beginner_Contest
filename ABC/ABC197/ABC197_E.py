# https://atcoder.jp/contests/abc197/submissions/21336563
# E - Traveler
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())
    XC = [list(map(int, input().split())) for _ in range(n)]

    XC.sort()
    tmp = [[] for _ in range(n)]
    for x, c in XC:
        tmp[c - 1].append(x)
    X = [x for x in tmp if x]

    dp = [[f_inf] * (len(X) + 1) for _ in range(2)]
    dp[0][0] = 0
    dp[1][0] = 0
    prev_l = prev_r = 0

    for i in range(1, len(X) + 1):
        now_l, now_r = X[i - 1][0], X[i - 1][-1]
        # 直前に左端にいて、最初に左端に向かった後右端に向かう
        if now_l > prev_l:
            ll = now_r - prev_l
        elif now_l < prev_l < now_r:
            ll = (prev_l - now_l) * 2 + (now_r - prev_l)
        else:
            ll = f_inf
        # 直前に右端にいて、最初に左端に向かった後右端に向かう
        if now_l > prev_r:
            rl = now_r - prev_r
        elif now_l < prev_r < now_r:
            rl = (prev_r - now_l) * 2 + (now_r - prev_r)
        else:
            rl = f_inf
        # 直前に左端にいて、最初に右端に向かった後左端に向かう
        if now_r < prev_l:
            lr = prev_l - now_l
        elif now_l < prev_l < now_r:
            lr = (now_r - prev_l) * 2 + (prev_l - now_l)
        else:
            lr = f_inf
        # 直前に右端にいて、最初に右端に向かった後左端に向かう
        if now_r < prev_r:
            rr = prev_r - now_l
        elif now_l < prev_r < now_r:
            rr = (now_r - prev_r) * 2 + (prev_r - now_l)
        else:
            rr = f_inf

        dp[0][i] = min(dp[0][i - 1] + lr, dp[1][i - 1] + rr)
        dp[1][i] = min(dp[0][i - 1] + ll, dp[1][i - 1] + rl)
        prev_l = now_l
        prev_r = now_r

    res = min(dp[0][-1] + abs(prev_l), dp[1][-1] + abs(prev_r))
    print(res)


if __name__ == '__main__':
    solve()
