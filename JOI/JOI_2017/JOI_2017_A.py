# https://atcoder.jp/contests/joi2017ho/submissions/17877957
# A - フェーン現象 (Foehn Phenomena)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, q, s, t = map(int, input().split())
    A = list(int(input()) for _ in range(n + 1))
    query = [list(map(int, input().split())) for _ in range(q)]

    D = [A[i + 1] - A[i] for i in range(n)]
    res = sum([diff * -s if diff > 0 else -diff * t for diff in D])
    for l, r, x in query:
        res += (D[l - 1] * s) if D[l - 1] > 0 else (D[l - 1] * t)
        D[l - 1] += x
        res += (-D[l - 1] * s) if D[l - 1] > 0 else (-D[l - 1] * t)

        if r != n:
            res += (D[r] * s) if D[r] > 0 else (D[r] * t)
            D[r] -= x
            res += (-D[r] * s) if D[r] > 0 else (-D[r] * t)

        print(res)


if __name__ == '__main__':
    resolve()
