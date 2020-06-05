# https://atcoder.jp/contests/abc036/submissions/13152903
# C - 座圧
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = sorted(list([int(input()), i] for i in range(n)), key=lambda x: x[0])

    dict = {}
    dict[A[0][0]] = 0
    diff = 0
    for i in range(1, n):
        if dict.get(A[i][0]) is None:
            diff += 1
            dict[A[i][0]] = diff

    A = sorted(A, key=lambda x: x[1])
    for i in range(n):
        print(dict[A[i][0]])


if __name__ == '__main__':
    resolve()
