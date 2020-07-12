# https://atcoder.jp/contests/joi2017yo/submissions/15203241
# A - 電子レンジ (Microwave)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    init = int(input())
    target = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    res = 0
    if init < 0:
        res += abs(init) * c + d
        res += target * e
    elif init == 0:
        res += d
        res += target * e
    else:
        res += (target - init) * e
    print(res)


if __name__ == '__main__':
    resolve()
