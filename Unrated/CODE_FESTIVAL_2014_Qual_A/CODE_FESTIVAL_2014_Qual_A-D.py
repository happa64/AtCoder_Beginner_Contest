# https://atcoder.jp/contests/code-festival-2014-quala/submissions/18851667
# D - 壊れた電卓
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = len(A)
    pow10 = [1]
    for i in range(n):
        pow10.append(pow10[-1] * 10)

    dp = [[[f_inf] * (1 << 10) for _ in range(n + 1)] for _ in range(3)]
    dp[1][0][0] = 0
    for i in range(1, n + 1):
        a = int(A[i - 1])
        for S in range(1 << 10):
            used = {mask for mask in range(10) if S & (1 << mask)}
            if len(used) > k:
                continue
            just_k = True if len(used) == k else False
            for num in range(10):
                if just_k and num not in used:
                    continue
                next_S = S | (1 << num)
                if num == a:
                    for flg in range(3):
                        dp[flg][i][next_S] = min(dp[flg][i][next_S], dp[flg][i - 1][S])
                else:
                    x = (num - a) * pow10[n - i]
                    dp[0][i][next_S] = min(dp[0][i][next_S], dp[0][i - 1][S] - x)
                    dp[2][i][next_S] = min(dp[2][i][next_S], dp[2][i - 1][S] + x)
                    if num < a:
                        dp[0][i][next_S] = min(dp[0][i][next_S], dp[1][i - 1][S] - x)
                    else:
                        dp[2][i][next_S] = min(dp[2][i][next_S], dp[1][i - 1][S] + x)

    res = int(A) - 10 ** (n - 1) + 1
    for S in range(1 << 10):
        if bin(S).count("1") > k:
            continue
        for flg in range(3):
            res = min(res, dp[flg][-1][S])
    print(res)


if __name__ == '__main__':
    A, k = input().split()
    k = min(len(A), int(k))
    resolve()
