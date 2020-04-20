# https://atcoder.jp/contests/abc142/tasks/abc142_e
# E - Get Everything
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    ABC = []
    for _ in range(m):
        a, b = map(int, input().split())
        C = list(map(int, input().split()))
        s = ["0"] * n
        for c in C:
            s[c - 1] = "1"
        c = "".join(s[::-1])
        ABC.append([a, b, int(c, 2)])

    # dp:宝箱の組み合わせiを全て開けられる鍵の買い方の最小コスト
    # 宝箱の組み合わせをbitで持つ
    dp = [f_inf for _ in range(1 << n)]
    dp[0] = 0
    for i in range(1 << n):
        for a, b, c in ABC:
            idx = i | c
            dp[idx] = min(dp[idx], dp[i] + a)

    if dp[-1] == f_inf:
        print(-1)
    else:
        print(dp[-1])


if __name__ == '__main__':
    resolve()
