# https://atcoder.jp/contests/abc074/submissions/14180209
# C - Sugar Water
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    A, B, C, D, E, F = map(int, input().split())
    W = set()
    for a in range(F // (100 * A) + 1):
        for b in range(F // (100 * B) + 1):
            if 0 < 100 * A * a + 100 * B * b <= F:
                W.add(100 * A * a + 100 * B * b)
    W = sorted(list(W))
    kouho = []
    for w in W:
        max_S = (w // 100) * E
        tmp = 0
        for c in range(0, max_S + 1, C):
            for d in range(0, max_S + 1 - c, D):
                s = c + d
                if s + w <= F:
                    tmp = max(tmp, s)
        kouho.append([w + tmp, tmp])

    ma = 0
    res = [W[0], 0]
    for total, sugar in kouho:
        noudo = (sugar * 100) / total
        if ma < noudo:
            ma = noudo
            res = [total, sugar]

    print(*res)


if __name__ == '__main__':
    resolve()
