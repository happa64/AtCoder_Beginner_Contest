# https://atcoder.jp/contests/abc050/tasks/abc050_b
# B - Contest with Drinks Easy
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    T = list(map(int, input().split()))
    m = int(input())

    for i in range(m):
        p, x = map(int, input().split())
        res = 0
        for j in range(n):
            if j == p - 1:
                res += x
            else:
                res += T[j]
        print(res)


if __name__ == '__main__':
    resolve()
