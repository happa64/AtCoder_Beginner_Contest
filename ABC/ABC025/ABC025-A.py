# https://atcoder.jp/contests/abc025/submissions/14105394
# A - 25個の文字列
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    t = int(input())

    def dfs(L):
        if len(L) == 2:
            res.append("".join(L))
            return

        for ss in s:
            L.append(ss)
            dfs(L)
            L.pop()

    res = []
    dfs([])
    print(res[t - 1])


if __name__ == '__main__':
    resolve()
