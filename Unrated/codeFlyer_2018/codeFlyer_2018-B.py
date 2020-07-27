# https://atcoder.jp/contests/bitflyer2018-qual/submissions/15490519
# B - 洋菓子店
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    A, B, N = map(int, input().split())
    X = input()

    for x in X:
        if x == "S":
            A -= 1
            A = max(0, A)
        elif x == "C":
            B -= 1
            B = max(0, B)
        else:
            if A > B:
                A -= 1
            elif B > A:
                B -= 1
            else:
                A -= 1
                A = max(0, A)
    print(A)
    print(B)


if __name__ == '__main__':
    resolve()
