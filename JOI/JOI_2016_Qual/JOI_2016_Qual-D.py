# https://atcoder.jp/contests/joi2016yo/submissions/15100348
# D - JOI国のお散歩事情 (Walking in JOI Kingdom)
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    N, T, Q = map(int, input().split())
    AD = [list(map(int, input().split())) for _ in range(N)]
    query = list(int(input()) for _ in range(Q))

    res = [0] * N
    left = right = 0
    while right < N:
        if AD[right][1] == 1:
            res[right] = AD[right][0] + T
            right += 1
        else:
            if right > 0 and AD[right - 1][1] == 1 and AD[right - 1][0] + T > AD[right][0] - T:
                t = (AD[right - 1][0] + AD[right][0]) // 2
                for i in range(left, right):
                    if AD[i][0] + T > t:
                        res[i] = t
                while right < N and AD[right][1] == 2 and AD[right][0] - T < t:
                    res[right] = t
                    right += 1
            else:
                res[right] = AD[right][0] - T
                right += 1
            left = right

    print(*[res[q - 1] for q in query], sep="\n")


if __name__ == '__main__':
    resolve()
