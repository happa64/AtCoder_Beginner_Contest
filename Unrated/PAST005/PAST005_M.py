# https://atcoder.jp/contests/past202012-open/submissions/19179066
# M - 棒の出荷
import sys
from itertools import accumulate
from bisect import bisect_left, bisect_right

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
        dp = [0] * (n + 2)
        dp[0], dp[1] = 1, -1
        for i in range(n + 1):
            dp[i] += dp[i - 1]
            if dp[i]:
                left = bisect_left(B, B[i] + x)
                right = bisect_right(B, B[i] + l)
                dp[left] += 1
                dp[right] -= 1
        return dp[n]

    n, l = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] + list(accumulate(A))

    ok, ng = 0, l + 1
    res = meguru_bisect(ok, ng)
    print(res)


if __name__ == '__main__':
    resolve()
