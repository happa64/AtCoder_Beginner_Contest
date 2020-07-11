# https://atcoder.jp/contests/aising2020/submissions/15141121
# A - Number of Multiples
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    L, R, d = map(int, input().split())
    res = 0
    for i in range(L, R + 1):
        if i % d == 0:
            res += 1
    print(res)


if __name__ == '__main__':
    resolve()
