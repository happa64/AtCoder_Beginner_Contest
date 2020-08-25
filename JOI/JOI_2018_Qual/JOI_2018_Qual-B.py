# https://atcoder.jp/contests/joi2018yo/submissions/16225388
# B - 双六 (Sugoroku)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    res = 1
    cnt = 0
    for i in range(n):
        if A[i] == 1:
            cnt += 1
            res = max(res, cnt + 1)
        else:
            cnt = 0
    print(res)


if __name__ == '__main__':
    resolve()
