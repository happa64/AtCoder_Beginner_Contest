# https://atcoder.jp/contests/pakencamp-2019-day3/submissions/17396716
# A - パ研合宿2103
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b = map(int, input().split())
    print(b - a + 1)


if __name__ == '__main__':
    resolve()
