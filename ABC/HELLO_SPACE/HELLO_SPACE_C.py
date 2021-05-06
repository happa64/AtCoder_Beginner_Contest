# https://atcoder.jp/contests/zone2021/submissions/22239996
# C - MAD TEAM
import sys
from itertools import combinations

sys.setrecursionlimit(10 ** 7)
if sys.platform == 'ios':
    sys.stdin = open('input_file.txt')
else:
    input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    def meguru_bisect(ok, ng):
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    def is_ok(x):
        bit = {tuple(p >= x for p in P[i]) for i in range(n)}
        bit = list(bit)

        for pattern in combinations(bit, min(3, len(bit))):
            t = [0] * 5
            for p in pattern:
                for i in range(5):
                    t[i] |= p[i]
            if 0 not in t:
                return True
        return False

    n = int(input())
    P = tuple(tuple(map(int, input().split())) for _ in range(n))

    ok, ng = 0, 10 ** 9 + 1
    res = meguru_bisect(ok, ng)
    print(res)


if __name__ == '__main__':
    solve()