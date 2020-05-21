# https://atcoder.jp/contests/abc134/submissions/13455221
# C - Exception Handling
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(int(input()) for _ in range(n))
    A_s = sorted(A)
    max_A = A_s[n - 1]
    sub_max_A = A_s[n - 2]

    for i in range(n):
        if A[i] == max_A:
            print(sub_max_A)
        else:
            print(max_A)


if __name__ == '__main__':
    resolve()
