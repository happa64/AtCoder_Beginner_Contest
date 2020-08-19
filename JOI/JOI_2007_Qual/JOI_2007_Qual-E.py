# https://atcoder.jp/contests/joi2007yo/submissions/16034728
# E - 品質検査
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b, c = map(int, input().split())
    n = int(input())
    R = [list(map(int, input().split())) for _ in range(n)]

    res = [2] * (a + b + c)
    for i, j, k, r in R:
        if r == 1:
            res[i - 1], res[j - 1], res[k - 1] = 1, 1, 1

    for i, j, k, r in R:
        if r == 0:
            if res[i - 1] == res[j - 1] == 1:
                res[k - 1] = 0
            elif res[i - 1] == res[k - 1] == 1:
                res[j - 1] = 0
            elif res[j - 1] == res[k - 1] == 1:
                res[i - 1] = 0

    print(*res, sep="\n")


if __name__ == '__main__':
    resolve()
