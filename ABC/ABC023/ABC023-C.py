# https://atcoder.jp/contests/abc023/submissions/16023288
# C - 収集王
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    r, c, k = map(int, input().split())
    n = int(input())
    candy = [list(map(int, input().split())) for _ in range(n)]

    R = [0] * r
    C = [0] * c
    for r, c in candy:
        R[r - 1] += 1
        C[c - 1] += 1

    cnt_R = defaultdict(int)
    for num in R:
        cnt_R[num] += 1

    cnt_C = defaultdict(int)
    for num in C:
        cnt_C[num] += 1

    res = 0
    for i in range(k + 1):
        res += cnt_R.get(i, 0) * cnt_C.get(k - i, 0)

    for i in range(n):
        r_, c_ = candy[i]
        sum_ = R[r_ - 1] + C[c_ - 1]
        if sum_ == k:
            res -= 1
        elif sum_ == k + 1:
            res += 1
    print(res)


if __name__ == '__main__':
    resolve()
