# https://atcoder.jp/contests/past202005/submissions/13506108
# D - 電光掲示板
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    S = list(list(input()) for _ in range(5))
    SS = []
    for i in range(n):
        L = []
        for h in range(5):
            subs = []
            for w in range(i * 4, i * 4 + 4):
                subs.append(1 if S[h][w] == "#" else 0)
            L.append(subs)
        SS.append(L)

    def solve(T):
        if T[0][1] == T[0][2] == T[0][3] == T[1][1] == T[1][3] == T[2][1] == T[2][3] == T[3][1] == T[3][3] == T[4][1] == T[4][2] == T[4][3] == 1 and T[2][2] == 0:
            return "0"
        elif T[0][2] == T[1][1] == T[1][2] == T[2][2] == T[3][2] == T[4][1] == T[4][2] == T[4][3] == 1:
            return "1"
        elif T[0][1] == T[0][2] == T[0][3] == T[1][3] == T[2][1] == T[2][2] == T[2][3] == T[3][1] == T[4][1] == T[4][2] == T[4][3] == 1 and T[1][1] == 0:
            return "2"
        elif T[0][1] == T[0][2] == T[0][3] == T[1][3] == T[2][1] == T[2][2] == T[2][3] == T[3][3] == T[4][1] == T[4][2] == T[4][3] == 1 and T[1][1] == 0:
            return "3"
        elif T[0][1] == T[0][3] == T[1][1] == T[1][3] == T[2][1] == T[2][2] == T[2][3] == T[3][3] == T[4][3] == 1 and T[0][2] == 0:
            return "4"
        elif T[0][1] == T[0][2] == T[0][3] == T[1][1] == T[2][1] == T[2][2] == T[2][3] == T[3][3] == T[4][1] == T[4][2] == T[4][3] == 1 and T[3][1] == T[1][3] == 0:
            return "5"
        elif T[0][1] == T[0][2] == T[0][3] == T[1][1] == T[2][1] == T[2][2] == T[2][3] == T[3][1] == T[3][3] == T[4][1] == T[4][2] == T[4][3] == 1 and T[1][3] == 0:
            return "6"
        elif T[0][1] == T[0][2] == T[0][3] == T[1][3] == T[2][3] == T[2][3] == T[3][3] == T[4][3] == 1 and T[1][1] == 0:
            return "7"
        elif T[0][1] == T[0][2] == T[0][3] == T[1][1] == T[1][3] == T[2][1] == T[2][2] == T[2][3] == T[3][1] == T[3][3] == T[4][1] == T[4][2] == T[4][3] == 1:
            return "8"
        elif T[0][1] == T[0][2] == T[0][3] == T[1][1] == T[1][3] == T[2][1] == T[2][2] == T[2][3] == T[3][3] == T[4][1] == T[4][2] == T[4][3] == 1:
            return "9"

    res = ""
    for num in SS:
        res += solve(num)

    print(res)


if __name__ == '__main__':
    resolve()
