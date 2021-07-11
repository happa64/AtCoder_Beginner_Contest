# https://atcoder.jp/contests/typical90/submissions/24159123
# 087 - Chokudai's Demand（★5）
import sys
from copy import deepcopy

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    def meguru_bisect(ok, ng, flg):
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if is_ok(mid, flg):
                ok = mid
            else:
                ng = mid
        return ok

    def is_ok(x, flg):
        A = deepcopy(init_A)
        for i in range(n):
            for j in range(n):
                if A[i][j] == -1:
                    A[i][j] = x
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    A[i][j] = min(A[i][j], A[i][k] + A[k][j])
        cnt = 0
        for i in range(n):
            for j in range(i + 1, n):
                if A[i][j] <= p:
                    cnt += 1
        return cnt >= K if not flg else cnt <= K

    n, p, K = map(int, input().split())
    init_A = [list(map(int, input().split())) for _ in range(n)]

    ok, ng = 0, 10 ** 18 + 1
    ma = meguru_bisect(ok, ng, 0)
    mi = meguru_bisect(ng, ok, 1)
    res = ma - mi + 1
    if res >= 2 * 10 ** 9:
        print("Infinity")
    else:
        print(res)


if __name__ == '__main__':
    solve()
