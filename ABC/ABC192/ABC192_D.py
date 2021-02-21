# https://atcoder.jp/contests/abc192/submissions/20362122?lang=ja
# D - Base n
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

    def is_ok(z):
        return to_n(x, z) <= m

    def to_n(x, n):
        res = 0
        d = 1
        for i in reversed(range(len(x))):
            res += int(x[i]) * d
            d *= n
        return res

    x = input().rstrip()
    m = int(input())
    d = int(max(list(str(x))))

    if int(x) <= 9:
        print(1 if int(x) <= m else 0)
    else:
        res = meguru_bisect(d, m + 1)
        print(res - d)


if __name__ == '__main__':
    resolve()
