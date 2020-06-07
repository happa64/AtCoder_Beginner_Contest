# https://atcoder.jp/contests/past202005/submissions/13507341
# C - 等比数列
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    A, R, N = map(int, input().split())

    if R == 1:
        print(A)
    else:
        res = A
        for i in range(N - 1):
            res *= R
            if res > 10 ** 9:
                print("large")
                break
        else:
            print(res)


if __name__ == '__main__':
    resolve()
