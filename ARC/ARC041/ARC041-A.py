# https://atcoder.jp/contests/arc041/submissions/14670129
# A - コインの反転
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x, y = map(int, input().split())
    k = int(input())

    if k <= y:
        print(x + k)
    else:
        k -= y
        x += y
        x -= k
        print(x)


if __name__ == '__main__':
    resolve()
