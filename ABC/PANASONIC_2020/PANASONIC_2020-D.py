# https://atcoder.jp/contests/panasonic2020/submissions/12881278
# D - String Equivalence
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())

    # S：文字を入れる配列、appear：登場済みの文字の種類
    def dfs(S, appear):
        if len(S) == n:
            print("".join(S))
            return

        for i in range(appear + 1):
            S.append(chr(97 + i))
            dfs(S, max(appear, i + 1))
            S.pop()

    dfs([], 0)


if __name__ == '__main__':
    resolve()
