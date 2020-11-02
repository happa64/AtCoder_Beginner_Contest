# https://atcoder.jp/contests/code-formula-2014-qualb/submissions/17843346
# D - お釣りの嫌いな高橋君
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(int(input()) for _ in range(n))

    block = []
    base = 1
    tot = 0
    prev = -1
    for i in range(n):
        tot += base * A[i]
        if pow(10, i - prev) > tot:
            block.append(tot + 1)
            tot = 0
            prev = i
            base = 1
        else:
            base *= 10

    block.append(tot + 1)

    res = 1
    for num in block:
        res *= num
        res %= mod
    print((res - 1) % mod)


if __name__ == '__main__':
    resolve()
