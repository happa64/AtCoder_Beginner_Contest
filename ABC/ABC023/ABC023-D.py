# https://atcoder.jp/contests/abc023/submissions/14943292
# D - 射撃王
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
        T = [0] * n
        for i in range(n):
            h, s = HS[i]
            if x - h < 0:
                return False
            T[i] = (x - h) // s
        T.sort()
        for i in range(n):
            if T[i] < i:
                return False
        return True

    n = int(input())
    HS = [list(map(int, input().split())) for _ in range(n)]

    ng, ok = 0, 10 ** 14
    res = meguru_bisect(ok, ng)
    print(res)


if __name__ == '__main__':
    resolve()
