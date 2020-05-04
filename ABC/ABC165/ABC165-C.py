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


# 再帰版
def resolve2():
    n, m, q = map(int, input().split())
    ABCD = [list(map(int, input().split())) for _ in range(q)]

    # 数列Aのスコアを返す
    def calc_score(L):
        score = 0
        for a, b, c, d in ABCD:
            if L[b - 1] - L[a - 1] == c:
                score += d
        return score

    # 数列Aを全パターン試す
    def dfs(A):
        if len(A) == n:
            return calc_score(A)

        res = 0
        prev = A[-1] if len(A) > 0 else 1
        for v in range(prev, m + 1):
            A.append(v)
            res = max(res, dfs(A))
            A.pop()

        return res

    print(dfs([]))


if __name__ == '__main__':
    resolve()
