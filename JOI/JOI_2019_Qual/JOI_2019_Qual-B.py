# https://atcoder.jp/contests/joi2019yo/submissions/16225743
# B - すごろくと駒 (Sugoroku and Pieces)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    X = list(map(int, input().split()))
    m = int(input())
    A = list(map(int, input().split()))

    for i in range(m):
        idx = A[i] - 1
        if X[idx] + 1 not in X and X[idx] + 1 != 2020:
            X[idx] += 1
    print(*X, sep="\n")

if __name__ == '__main__':
    resolve()
