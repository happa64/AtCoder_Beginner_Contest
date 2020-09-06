# https://atcoder.jp/contests/ddcc2020-qual/submissions/16533848
# D - Digit Sum Replace
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    m = int(input())
    DC = [list(map(int, input().split())) for _ in range(m)]
    total = 0
    res = 0
    for d, c in DC:
        r = c * d
        res += c
        while r // 10:
            q, r = divmod(r, 10)
            res += q
            r += q
        total += r

    while total // 10:
        q, total = divmod(total, 10)
        res += q
        total += q

    print(res - 1)


if __name__ == '__main__':
    resolve()
