# https://atcoder.jp/contests/abc002/tasks/abc002_3
# C - 直訴
import sys

sys.setrecursionlimit(10 ** 7)


def resolve():
    xa, ya, xb, yb, xc, yc = map(int, input().split())
    a = pow(pow(xa - xb, 2) + pow(ya - yb, 2), 0.5)
    b = pow(pow(xb - xc, 2) + pow(yb - yc, 2), 0.5)
    c = pow(pow(xc - xa, 2) + pow(yc - ya, 2), 0.5)
    s = (a + b + c) / 2
    S = pow(s * (s - a) * (s - b) * (s - c), 0.5)
    print(S)


if __name__ == '__main__':
    resolve()
