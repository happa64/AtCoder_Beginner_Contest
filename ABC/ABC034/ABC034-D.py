# https://atcoder.jp/contests/abc034/submissions/14084989
# D - 食塩水
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    WP = []
    for _ in range(n):
        w, p = map(int, input().split())
        nacl = w * p / 100
        WP.append([nacl, w])

    # 食塩水の濃度 x = sum(nacl) / sum(w)を最大化したい
    # xを二分探索して考える
    # x <= sum(nacl) / sum(w)を変形し、sum(nacl) - x * sum(w) >= 0となればよい
    def is_ok(x):
        res = []
        for i in range(n):
            nacl, w = WP[i]
            res.append(nacl - x * w)
        res.sort(reverse=True)
        ma = sum(res[:k])
        return ma >= 0

    def meguru_bisect(ok, ng):
        """
        is_okを定義して下さい
        :param ok: 取りうる最小の値-1
        :param ng: 取りうる最大の値+1
        :return: is_okを満たす最小(もしくは最大)の値
        """
        while abs(ok - ng) > 10 ** (-7):
            mid = (ok + ng) / 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    ok = -1
    ng = 101
    print(meguru_bisect(ok, ng) * 100)


if __name__ == '__main__':
    resolve()
