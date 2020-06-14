# https://atcoder.jp/contests/abc128/submissions/13207169
# A - Apple Pie
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, p = map(int, input().split())
    mate = a * 3 + p
    print(mate // 2)


if __name__ == '__main__':
    resolve()
