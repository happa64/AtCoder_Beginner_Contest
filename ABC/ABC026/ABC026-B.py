# https://atcoder.jp/contests/abc026/submissions/13993372
# B - N重丸
import sys
import math

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    R = sorted(list(int(input()) for _ in range(n)), reverse=True)

    flg = 1
    res = 0
    for i in range(n):
        if flg:
            res += pow(R[i], 2) * math.pi
        else:
            res -= pow(R[i], 2) * math.pi
        flg ^= 1
    print(res)


if __name__ == '__main__':
    resolve()
