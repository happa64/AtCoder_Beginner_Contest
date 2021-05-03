# https://atcoder.jp/contests/typical90/submissions/21907463
# 001 - Yokan Party（★4）
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    def meguru_bisect(ok, ng):
        """
        is_okを定義して下さい
        :param ok: 取りうる最小の値-1
        :param ng: 取りうる最大の値+1
        :return: is_okを満たす最小(もしくは最大)の値
        """
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    def is_ok(x):
        cnt = 0
        now = 0
        for a in A:
            if now + a >= x:
                cnt += 1
                now = 0
            else:
                now += a
        return cnt >= k + 1

    n, l = map(int, input().split())
    k = int(input())
    A = [0] + list(map(int, input().split())) + [l]
    A = [b - a for a, b in zip(A, A[1:])]

    ok, ng = 0, 10 ** 14 + 1
    res = meguru_bisect(ok, ng)
    print(res)


if __name__ == '__main__':
    solve()
