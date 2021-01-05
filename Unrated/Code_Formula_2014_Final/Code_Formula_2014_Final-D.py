# https://atcoder.jp/contests/code-formula-2014-final/submissions/19216109
# D - 映画の連続視聴
import sys
from itertools import accumulate
from bisect import bisect_left

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    H = list(accumulate(map(int, input().split())))
    M = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[2])
    T = sorted(set(M[i][1] for i in range(n)) | set(M[i][2] for i in range(n)))
    for i in range(n):
        _, s, e = M[i]
        M[i][1] = bisect_left(T, s)
        M[i][2] = bisect_left(T, e)

    dp = [0] * (M[-1][2] + 1)
    prev = 1
    for i in range(n):
        m, s, e = M[i]
        for j in range(prev, e + 1):
            dp[j] = max(dp[j], dp[j - 1])
        dp[e] = max(dp[e], dp[s] + H[0])
        prev = e + 1
        cnt = 0
        for nm, ns, ne in M[i + 1:]:
            if nm == m and e <= ns:
                cnt += 1
                dp[ne] = max(dp[ne], dp[s] + H[cnt])
                e = ne
    print(max(dp))


if __name__ == '__main__':
    resolve()
