# https://atcoder.jp/contests/abc174/submissions/15594369
# B - Distance
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, d = map(int, input().split())
    res = 0
    for _ in range(n):
        x, y = map(int, input().split())
        dist = pow(x, 2) + pow(y, 2)
        if dist <= pow(d, 2):
            res += 1
    print(res)


if __name__ == '__main__':
    resolve()
