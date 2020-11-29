# https://atcoder.jp/contests/arc109/submissions/18459940
# B - log
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
        m = n + 1 - (x - 1)
        t = (n + 1 + m) * x // 2
        if t >= tot:
            return True
        else:
            return False

    n = int(input())
    tot = (n + 1) * n // 2

    ng, ok = 0, n + 1
    res = meguru_bisect(ok, ng)
    print(res)


if __name__ == '__main__':
    resolve()
