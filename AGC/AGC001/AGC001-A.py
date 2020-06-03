# https://atcoder.jp/contests/agc001/submissions/13213181
# A - BBQ Easy
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    L = sorted(list(map(int, input().split())))

    res = 0
    for i in range(n * 2):
        if i % 2 == 0:
            res += L[i]
    print(res)


if __name__ == '__main__':
    resolve()
