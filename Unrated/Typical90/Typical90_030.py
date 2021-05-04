# https://atcoder.jp/contests/typical90/submissions/22295522
# 030 - K Factors（★5）
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n, k = map(int, input().split())
    res = [0] * (n + 1)
    for i in range(2, n + 1):
        if res[i]:
            continue
        for j in range(i, n + 1, i):
            res[j] += 1
    res = sum(res[i] >= k for i in range(n + 1))
    print(res)


if __name__ == '__main__':
    solve()
