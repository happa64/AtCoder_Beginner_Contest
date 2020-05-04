# https://atcoder.jp/contests/abc166/tasks/abc166_d
# D - I hate Factorization
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x = int(input())

    for b in range(10 ** 3):
        for a in range(10 ** 3):
            if pow(a, 5) - pow(b, 5) == x:
                print(a, b)
                exit()
            if pow(-a, 5) - pow(b, 5) == x:
                print(-a, b)
                exit()
            if pow(a, 5) - pow(-b, 5) == x:
                print(a, -b)
                exit()
            if pow(-a, 5) - pow(-b, 5) == x:
                print(-a, -b)
                exit()


if __name__ == '__main__':
    resolve()
