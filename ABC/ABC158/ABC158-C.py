# https://atcoder.jp/contests/abc158/submissions/13404641
# C - Tax Increase
import sys
import math
sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b = map(int, input().split())

    for i in range(1, 10 ** 4):
        if math.floor(i * 0.08) == a and math.floor(i * 0.1) == b:
            print(i)
            break
    else:
        print(-1)


if __name__ == '__main__':
    resolve()
