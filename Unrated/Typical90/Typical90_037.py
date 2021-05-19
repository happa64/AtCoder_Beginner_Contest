# https://atcoder.jp/contests/typical90/submissions/22524114
# 037 - Don't Leave the Spice（★5）
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    W, n = map(int, input().split())
    dp = [-f_inf] * (W + 1)
    dp[0] = 0
    for _ in range(n):
        l, r, v = map(int, input().split())
        k = r - l + 1
        next_dp = [-f_inf] * (W + 1)
        que = deque([])
        for w in range(W + 1):
            next_dp[w] = max(next_dp[w], dp[w])
            while que and que[0] <= w - k:
                que.popleft()
            while que and dp[que[-1]] + v < dp[w] + v:
                que.pop()
            que.append(w)
            if w + l <= W:
                next_dp[w + l] = max(next_dp[w + l], dp[que[0]] + v)
        dp = next_dp
    print(dp[-1] if dp[-1] != -f_inf else -1)


if __name__ == '__main__':
    solve()
