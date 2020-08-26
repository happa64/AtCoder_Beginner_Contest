# https://atcoder.jp/contests/agc006/submissions/16243935
# B - Median Pyramid Easy
import sys
from statistics import median

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7
res = 0


def resolve():
    def dfs(S):
        """ デバッグ用 """
        global res
        if len(S) == 1:
            res = S[0]
            return
        tmp = []
        for i in range(1, len(S) - 1):
            t = median([S[i - 1], S[i], S[i + 1]])
            tmp.append(t)
        dfs(tmp)

    n, x = map(int, input().split())
    if x == 1 or x == 2 * n - 1:
        print("No")
        exit()
    n = 2 * n - 1
    ans = [0] * n
    num = x
    for i in range(n // 2, n):
        ans[i] = num
        num += 1
        if num > n:
            num = 1
    for i in range(n // 2):
        ans[i] = num
        num += 1
        if num > n:
            num = 1
    print("Yes")
    print(*ans, sep="\n")
    # dfs(ans)
    # print(res == x)


if __name__ == '__main__':
    resolve()
