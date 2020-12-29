# https://atcoder.jp/contests/past202012-open/submissions/19042682
# L - T消し
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    N = int(input())
    S = input()
    T = input()

    dp = [[-1] * (N + 1) for _ in range(N + 1)]

    def dfs(l, r, dp):
        if dp[l][r] >= 0:
            return dp[l][r]
        if r - l < 3:
            dp[l][r] = 0
            return dp[l][r]
        if r - l == 3:
            if S[l:r] == T:
                dp[l][r] = 3
            else:
                dp[l][r] = 0
            return dp[l][r]
        ans = 0
        for mid in range(l + 1, r):
            ans = max(ans, dfs(l, mid, dp) + dfs(mid, r, dp))
            if S[l] == T[0] and S[mid] == T[1] and S[r - 1] == T[2]:
                if dfs(l + 1, mid, dp) == mid - l - 1 and dfs(mid + 1, r - 1, dp) == r - mid - 2:
                    ans = r - l
                    break
        dp[l][r] = ans
        return ans

    ans = dfs(0, N, dp) // 3
    print(ans)


if __name__ == '__main__':
    resolve()
