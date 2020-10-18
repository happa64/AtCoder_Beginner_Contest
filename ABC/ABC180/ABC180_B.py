# https://atcoder.jp/contests/abc180/submissions/17440303
# B - Various distances
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    X = list(map(int, input().split()))

    res = 0
    for x in X:
        res += abs(x)
    print(res)

    res2 = 0
    for x in X:
        res2 += pow(x, 2)
    print(pow(res2, 0.5))

    res3 = max([abs(x) for x in X])
    print(res3)


if __name__ == '__main__':
    resolve()
