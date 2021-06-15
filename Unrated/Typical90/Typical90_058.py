# https://atcoder.jp/contests/typical90/submissions/23170016
# 058 - Original Calculator（★4）
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def digit_sum(x):
    res = sum(int(i) for i in str(x))
    return res


def solve():
    n, k = map(int, input().split())

    x = n
    d = 0
    dist = [-1] * 100000
    while True:
        if x == 0:
            print(0)
            exit()
        if k == 0:
            print(x)
            exit()
        if dist[x] == -1:
            dist[x] = d
            x = (x + digit_sum(x)) % 100000
            d += 1
            k -= 1
        else:
            break

    step = d - dist[x]
    k %= step
    for _ in range(k):
        x = (x + digit_sum(x)) % 100000
    print(x)


if __name__ == '__main__':
    solve()
