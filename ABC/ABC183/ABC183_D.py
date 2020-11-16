# https://atcoder.jp/contests/abc183/submissions/18134853
# D - Water Heater
import sys
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, w = map(int, input().split())
    query = [list(map(int, input().split())) for _ in range(n)]
    imos = [0] * (2 * 10 ** 5 + 10)

    for s, t, p in query:
        imos[s] += p
        imos[t] -= p

    imos = list(accumulate(imos))
    for i in range(len(imos)):
        if imos[i] > w:
            print("No")
            break
    else:
        print("Yes")


if __name__ == '__main__':
    resolve()
