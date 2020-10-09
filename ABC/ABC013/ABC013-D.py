# https://atcoder.jp/contests/abc013/submissions/17270800
# D - 阿弥陀
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m, d = map(int, input().split())
    A = list(map(int, input().split()))
    L = d.bit_length()

    pos = list(range(1, n + 1))
    for a in A:
        t = pos[a - 1]
        pos[a - 1] = pos[a]
        pos[a] = t

    init = [0] * n
    for idx, p in enumerate(pos, 1):
        init[p - 1] = idx

    step = [[0] * n for _ in range(L)]
    step[0] = [init[i - 1] - i for i in range(1, n + 1)]
    for i in range(1, L):
        for j in range(n):
            step[i][j] = step[i - 1][j] + step[i - 1][j + step[i - 1][j]]

    prev = list(range(1, n + 1))
    for mask in range(L):
        if d & (1 << mask):
            nxt = [0] * n
            for i in range(n):
                nxt[i + step[mask][i]] = prev[i]
            prev = nxt

    res = [0] * n
    for idx, p in enumerate(prev, 1):
        res[p - 1] = idx

    print(*res, sep="\n")


if __name__ == '__main__':
    resolve()
