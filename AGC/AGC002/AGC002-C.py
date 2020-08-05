# https://atcoder.jp/contests/agc002/submissions/15705119
# C - Knot Puzzle
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, L = map(int, input().split())
    A = list(map(int, input().split()))

    init = -1
    for i in range(1, n):
        if A[i] + A[i - 1] >= L:
            init = i
            break
    else:
        print("Impossible")
        exit()
    res = []
    for i in range(1, init):
        res.append(i)

    for i in reversed(range(init + 1, n)):
        res.append(i)
    res.append(init)
    print("Possible")
    print(*res, sep="\n")


if __name__ == '__main__':
    resolve()
