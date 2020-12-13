# https://atcoder.jp/contests/abc185/submissions/18727924
# B - Smartphone Addiction
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m, t = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(m)]

    remain = n
    now = 0
    for a, b in AB:
        diff = a - now
        if remain - diff <= 0:
            print("No")
            break
        else:
            remain -= diff
            remain = min(n, remain + b - a)
            now = b
    else:
        diff = t - now
        if remain - diff <= 0:
            print("No")
        else:
            print("Yes")


if __name__ == '__main__':
    resolve()
