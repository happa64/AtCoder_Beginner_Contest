# https://atcoder.jp/contests/abc076/submissions/17917562
# D - AtCoder Express
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    T = list(map(int, input().split()))
    V = list(map(int, input().split()))

    tot = sum(T) * 2 + 1

    max_V = [f_inf] * tot
    now = 0
    for i in range(n):
        for t in range(T[i] * 2):
            t += now
            max_V[t] = min(max_V[t], V[i])
        now += T[i] * 2
        max_V[now] = min(max_V[now], V[i])
    max_V[0] = max_V[-1] = 0

    for i in range(1, tot):
        max_V[i] = min(max_V[i], max_V[i - 1] + 0.5)

    for i in reversed(range(tot - 1)):
        max_V[i] = min(max_V[i], max_V[i + 1] + 0.5)

    res = 0
    for i in range(1, tot):
        res += (max_V[i - 1] + max_V[i]) / 4
    print(res)


if __name__ == '__main__':
    resolve()
