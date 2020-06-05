# https://atcoder.jp/contests/code-festival-2016-qualc/submissions/14026377
# C - 二人のアルピニスト
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    T = list(map(int, input().split()))
    A = list(map(int, input().split()))

    pattern = [0] * n
    prev = -f_inf
    for i in range(n):
        if prev < T[i]:
            pattern[i] = 1
            prev = T[i]

    prev = -f_inf
    for i in reversed(range(n)):
        if prev < A[i]:
            if pattern[i] != 0 and T[i] != A[i]:
                print(0)
                exit()
            pattern[i] = 1
            prev = A[i]
        else:
            if pattern[i] != 0 and T[i] > A[i]:
                print(0)
                exit()

    res = 1
    for i in range(n):
        if pattern[i] == 0:
            pattern[i] = min(T[i], A[i])
        res = res * pattern[i] % mod
    print(res)


if __name__ == '__main__':
    resolve()
