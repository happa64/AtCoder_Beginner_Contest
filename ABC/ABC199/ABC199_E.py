# https://atcoder.jp/contests/abc199/submissions/22295320
# E - Permutation
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n, m = map(int, input().split())
    XYZ = [list(map(int, input().split())) for _ in range(m)]

    dp = [0] * (1 << n)
    dp[0] = 1
    for i in range(1 << n):
        used = bin(i).count("1")
        cnt = [0] * (n + 1)
        for num in range(1, n + 1):
            if i & (1 << (num - 1)):
                cnt[num] += 1
            cnt[num] += cnt[num - 1]
        mi = 0
        for x, y, z in XYZ:
            if used >= x:
                continue
            if cnt[y] > z:
                break
            elif cnt[y] == z:
                mi = max(mi, y)
        else:
            for j in range(mi, n):
                if i & (1 << j):
                    continue
                dp[i | (1 << j)] += dp[i]
    print(dp[-1])


if __name__ == '__main__':
    solve()
