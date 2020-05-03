# https://atcoder.jp/contests/abc165/tasks/abc165_c
# C - Many Requirements
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7
ans = 0


def resolve():
    n, m, q = map(int, input().split())
    ABCD = [list(map(int, input().split())) for _ in range(q)]

    A = [0] * n

    def dfs(idx):
        global ans
        if idx == n:
            score = 0
            for i in range(q):
                a, b, c, d = ABCD[i]
                if A[b - 1] - A[a - 1] == c:
                    score += d
            ans = max(ans, score)
        else:
            if idx == 0:
                k = 1
            else:
                k = A[idx - 1]

            for i in range(k, m + 1):
                A[idx] = i
                dfs(idx + 1)

    dfs(0)
    print(ans)


if __name__ == '__main__':
    resolve()
