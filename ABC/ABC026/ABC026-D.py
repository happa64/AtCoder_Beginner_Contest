# https://atcoder.jp/contests/abc026/submissions/14105988
# D - 高橋君ボール1号
import sys
import math
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def is_ok(t):
        f = a * t + b * math.sin(c * t * math.pi)
        return 100 - f <= 0

    def meguru_bisect(ok, ng):
        while abs(ok - ng) > 10 ** (-12):
            mid = (ok + ng) / 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    a, b, c = map(int, input().split())

    ok = 101
    ng = -1
    t = meguru_bisect(ok, ng)
    print(t)


if __name__ == '__main__':
    resolve()
