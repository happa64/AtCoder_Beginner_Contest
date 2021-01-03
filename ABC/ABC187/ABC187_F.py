# https://atcoder.jp/contests/abc187/submissions/19176210
# F - Close Group
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    E = [0] * n
    for _ in range(m):
        a, b = map(lambda x: int(x) - 1, input().split())
        E[a] |= 1 << b
        E[b] |= 1 << a

    dp = [f_inf] * (1 << n)
    dp[0] = 0
    for i in range(1 << n):
        for j in range(n):
            if not (i & (1 << j)):
                continue
            target = i ^ (1 << j)
            if dp[target] <= 1 and (E[j] & target) == target:
                dp[i] = 1

    for i in range(1 << n):
        j = (i - 1) & i
        while j > 0:
            dp[i] = min(dp[i], dp[j] + dp[i ^ j])
            j = (j - 1) & i
    print(dp[-1])


if __name__ == '__main__':
    resolve()
