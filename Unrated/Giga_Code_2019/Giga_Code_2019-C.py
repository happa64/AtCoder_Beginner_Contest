# https://atcoder.jp/contests/gigacode-2019/submissions/15235039
# C - パソコンの購入
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    D = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    money = 0
    res = []
    for i in range(D):
        money += A[i]
        if money >= B[i]:
            res.append(B[i])

    if len(res) == 0:
        print(-1)
    else:
        print(min(res))


if __name__ == '__main__':
    resolve()
