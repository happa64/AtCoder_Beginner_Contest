# https://atcoder.jp/contests/abc174/submissions/15656549
# E - Logs
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def meguru_bisect(ok, ng):
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    def is_ok(x):
        cnt = 0
        for i in range(n):
            if A[i] > x:
                cnt += (A[i] + x - 1) // x - 1
        return cnt <= k

    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    res = meguru_bisect(10 ** 9 + 1, 0)
    print(res)


if __name__ == '__main__':
    resolve()
