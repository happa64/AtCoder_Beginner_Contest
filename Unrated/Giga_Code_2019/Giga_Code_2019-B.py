# https://atcoder.jp/contests/gigacode-2019/submissions/15226218
# B - 採用面接
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, x, y, z = map(int, input().split())

    res = 0
    for _ in range(n):
        a, b = map(int, input().split())
        if a >= x and b >= y and a + b >= z:
            res += 1
    print(res)


if __name__ == '__main__':
    resolve()
