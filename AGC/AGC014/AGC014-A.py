# https://atcoder.jp/contests/agc014/tasks/agc014_a
# A - Cookie Exchanges
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    A, B, C = map(int, input().split())

    if A == B == C and A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
        print(-1)
    else:
        res = 0
        while A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
            a = B // 2 + C // 2
            b = A // 2 + C // 2
            c = A // 2 + B // 2
            A, B, C = a, b, c
            res += 1

        print(res)


if __name__ == '__main__':
    resolve()
