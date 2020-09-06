# https://atcoder.jp/contests/code-festival-2015-quala/submissions/16541434
# D - 壊れた電車
import sys

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
        left = -1
        for i in range(m):
            now = X[i] - 1
            if X[i] - 1 <= left:
                left = max(left, now + x)
            else:
                if left < now - x - 1:
                    return False
                else:
                    now1 = x - now + 2 * (left + 1)
                    now2 = (x + now + left + 1) // 2
                    left = max(left, max(now1, now2))
        return left >= n - 1

    n, m = map(int, input().split())
    X = list(int(input()) for _ in range(m))
    ng, ok = -1, 10 ** 10
    res = meguru_bisect(ok, ng)
    print(res)


if __name__ == '__main__':
    resolve()
