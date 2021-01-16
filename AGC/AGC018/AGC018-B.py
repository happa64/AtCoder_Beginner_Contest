# https://atcoder.jp/contests/agc018/submissions/16171594
# B - Sports Festival
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7
res = f_inf


def resolve():
    def dfs(remove):
        global res
        if len(remove) == m:
            return

        cnt = [0] * m
        ma = -f_inf
        target = None
        for i in range(n):
            for j in range(m):
                if A[i][j] not in remove:
                    cnt[A[i][j] - 1] += 1
                    if ma < cnt[A[i][j] - 1]:
                        ma = cnt[A[i][j] - 1]
                        target = A[i][j]
                    break

        remove.insert(target)
        res = min(res, ma)
        dfs(remove)

    n, m = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]

    dfs(set())
    print(res)


if __name__ == '__main__':
    resolve()
