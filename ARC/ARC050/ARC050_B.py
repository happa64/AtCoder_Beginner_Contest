# https://atcoder.jp/contests/arc050/submissions/16758073
# B - 花束
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

    def is_ok(k):
        if R - k < 0 or B - k < 0:
            return False
        a = (R - k) // (x - 1)
        b = (B - k) // (y - 1)
        return a + b >= k

    R, B = map(int, input().split())
    x, y = map(int, input().split())

    ok, ng = -1, 10 ** 19
    res = meguru_bisect(ok, ng)
    print(res)


if __name__ == '__main__':
    resolve()
