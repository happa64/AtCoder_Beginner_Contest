# https://atcoder.jp/contests/abc013/submissions/16015726
# C - 節制
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
        ret = 0
        cnt_a = x // a
        for i in range(cnt_a + 1):
            now_x = x - i * a
            now_h = h + i * b

            cnt_b = now_x // c
            now_h += cnt_b * d

            cnt_e = now_h // e
            if now_h % e == 0:
                cnt_e -= 1
            ret = max(ret, i + cnt_b + cnt_e)

        return ret >= n

    n, h = map(int, input().split())
    a, b, c, d, e = map(int, input().split())

    ng, ok = -1, n * max(a, c) + 1
    res = meguru_bisect(ok, ng)
    print(res)


if __name__ == '__main__':
    resolve()
