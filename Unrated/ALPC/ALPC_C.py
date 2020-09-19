# https://atcoder.jp/contests/practice2/submissions/16574200
# C - Floor Sum
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def floor_sum(n, m, a, b):
    res = 0
    if a >= m:
        res += (n - 1) * n * (a // m) // 2
        a %= m
    if b >= m:
        res += n * (b // m)
        b &= m
    y_max = (a * n + b) // m
    x_max = (y_max * m - b)
    if y_max == 0:
        return res
    res += (n - (x_max + a - 1) // a) * y_max
    res += floor_sum(y_max, a, m, (a - x_max % a) % a)
    return res


def resolve():
    t = int(input())
    for _ in range(t):
        n, m, a, b = map(int, input().split())
        print(floor_sum(n, m, a, b))


if __name__ == '__main__':
    resolve()
