# https://atcoder.jp/contests/joi2015ho/submissions/16990801
# A - 鉄道旅行 (Railroad Trip)
import sys
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    P = list(map(int, input().split()))
    ABC = [list(map(int, input().split())) for _ in range(n - 1)]

    imos = [0] * n
    for i in range(m - 1):
        left, right = P[i], P[i + 1]
        left, right = min(left, right) - 1, max(left, right) - 2
        imos[left] += 1
        imos[right + 1] -= 1

    imos = list(accumulate(imos))[:n - 1]
    res = 0
    for i in range(n - 1):
        cnt = imos[i]
        a, b, c = ABC[i]
        cost = min(cnt * a, cnt * b + c)
        res += cost
    print(res)


if __name__ == '__main__':
    resolve()
