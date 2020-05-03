# https://atcoder.jp/contests/abc165/tasks/abc165_c
# C - Many Requirements
import sys
import itertools

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m, q = map(int, input().split())
    ABCD = [list(map(int, input().split())) for _ in range(q)]

    res = 0
    # 重複無し順列を全列挙
    for pattern in itertools.combinations_with_replacement(range(1, m + 1), n):
        score = 0
        for a, b, c, d in ABCD:
            if pattern[b - 1] - pattern[a - 1] == c:
                score += d
        res = max(res, score)

    print(res)


if __name__ == '__main__':
    resolve()
