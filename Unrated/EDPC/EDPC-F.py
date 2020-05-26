# https://atcoder.jp/contests/dp/submissions/13611964
# F - LCS
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S = list(input())
    T = list(input())

    LCS = [[0 for _ in range(len(T) + 1)] for _ in range(len(S) + 1)]
    for i in range(1, len(S) + 1):
        for j in range(1, len(T) + 1):
            x = 1 if S[i - 1] == T[j - 1] else 0
            LCS[i][j] = max(LCS[i - 1][j - 1] + x, LCS[i - 1][j], LCS[i][j - 1])

    res = []
    i, j = len(S), len(T)
    while i > 0 and j > 0:
        if LCS[i][j] == LCS[i - 1][j]:
            i -= 1
        elif LCS[i][j] == LCS[i][j - 1]:
            j -= 1
        else:
            res.append(S[i - 1])
            i -= 1
            j -= 1

    print("".join(res[::-1]))


if __name__ == '__main__':
    resolve()
