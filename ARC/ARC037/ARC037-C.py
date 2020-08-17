# https://atcoder.jp/contests/arc037/submissions/16010536
# C - 億マス計算
import sys
from bisect import bisect_right

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
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
        for a in A:
            t = x // a
            cnt += bisect_right(B, t)
        return cnt < k

    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    ng, ok = 0, A[-1] * B[-1]
    res = meguru_bisect(ng, ok) + 1
    print(res)


if __name__ == '__main__':
    resolve()
