# https://atcoder.jp/contests/mujin-pc-2016/submissions/13593435
# B - ロボットアーム
import sys
import math

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b, c = map(int, input().split())

    ma = pow(a + b + c, 2) * math.pi

    if a + b > c and b + c > a and c + a > b:
        mi = 0
    elif a + b <= c:
        mi = pow(a + b - c, 2) * math.pi
    elif b + c <= a:
        mi = pow(b + c - a, 2) * math.pi
    elif c + a <= b:
        mi = pow(a + c - b, 2) * math.pi

    print(ma - mi)


if __name__ == '__main__':
    resolve()
