# https://atcoder.jp/contests/abc071/submissions/12918000
# D - Coloring Dominoes
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    S1 = input()
    S2 = input()

    Domino = []
    i = 0
    while i < n:
        if S1[i] == S2[i]:
            Domino.append("X")
            i += 1
        else:
            Domino.append("Y")
            i += 2

    res = 3 if Domino[0] == "X" else 6
    for i in range(1, len(Domino)):
        if Domino[i] == "X" and Domino[i - 1] == "X":
            res = res * 2 % mod
        elif Domino[i] == "X" and Domino[i - 1] == "Y":
            pass
        elif Domino[i] == "Y" and Domino[i - 1] == "X":
            res = res * 2 % mod
        else:
            res = res * 3 % mod

    print(res)


if __name__ == '__main__':
    resolve()
