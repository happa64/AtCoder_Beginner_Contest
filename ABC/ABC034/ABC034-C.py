# https://atcoder.jp/contests/abc034/submissions/13939891
# C - 経路
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    W, H = map(int, input().split())
    W -= 1
    H -= 1

    fact = [0, 1]
    for i in range(2, H + W + 1):
        fact.append(fact[-1] * i % mod)

    res = (fact[H + W] * pow(fact[H] * fact[W], mod - 2, mod)) % mod
    print(res)


if __name__ == '__main__':
    resolve()
