# https://atcoder.jp/contests/abc038/submissions/13102267
# C - 単調増加
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    res = 1
    cnt = 1
    for i in range(1, n):
        res += 1
        if A[i - 1] < A[i]:
            cnt += 1
        else:
            res += (cnt * (cnt - 1)) // 2
            cnt = 1

    if cnt > 0:
        res += (cnt * (cnt - 1)) // 2

    print(res)


if __name__ == '__main__':
    resolve()
