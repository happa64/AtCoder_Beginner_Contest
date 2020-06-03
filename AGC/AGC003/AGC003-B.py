# https://atcoder.jp/contests/agc003/submissions/12946004
# B - Simplified mahjong
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = [0] + list(int(input()) for _ in range(n)) + [0]

    res = 0
    cnt = 0
    for i in range(n + 2):
        if A[i] == 0:
            res += cnt // 2
            cnt = 0
        else:
            cnt += A[i]

    print(res)


if __name__ == '__main__':
    resolve()
