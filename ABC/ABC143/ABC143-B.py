# https://atcoder.jp/contests/abc143/submissions/14381469
# B - TAKOYAKI FESTIVAL 2019
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    D = list(map(int, input().split()))

    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            res += D[i] * D[j]
    print(res)


if __name__ == '__main__':
    resolve()
