# https://atcoder.jp/contests/abc093/submissions/20244704
# D - Worst Case
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    q = int(input())
    query = [list(map(int, input().split())) for _ in range(q)]

    for a, b in query:
        if a == b == 1:
            print(0)
            continue
        a, b = min(a, b), max(a, b)
        limit = a * b - 1
        x = int(pow(limit, 0.5))
        y = limit // x
        x, y = min(x, y), max(x, y)
        res = x * 2
        if x == y:
            res -= 1
        if a <= x:
            res -= 1
        if b <= x:
            res -= 1
        print(res)


if __name__ == '__main__':
    resolve()
