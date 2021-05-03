# https://atcoder.jp/contests/typical90/submissions/22251129
# 006 - Smallest Subsequence（★5）
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n, k = map(int, input().split())
    s = input().rstrip()

    c = [[f_inf] * 26 for _ in range(n + 1)]
    for i in reversed(range(n)):
        idx = ord(s[i]) - ord("a")
        c[i][idx] = i
        for j in range(26):
            if j == idx:
                continue
            c[i][j] = c[i + 1][j]

    res = ""
    i = 0
    while k:
        for j in range(26):
            left = n - c[i][j]
            if left >= k:
                res += chr(ord("a") + j)
                k -= 1
                i = c[i][j] + 1
                break
    print(res)


if __name__ == '__main__':
    solve()
