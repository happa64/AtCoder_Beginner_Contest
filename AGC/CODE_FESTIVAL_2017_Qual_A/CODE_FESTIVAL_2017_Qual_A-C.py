# https://atcoder.jp/contests/code-festival-2017-quala/submissions/12977393
# C - Palindromic Matrix
import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        a = list(input())
        A.extend(a)

    D = Counter(A)
    B = [["" for _ in range(W)] for _ in range(H)]
    if H > 1 and W > 1:
        for h in range(H // 2):
            for w in range(W // 2):
                for k, v in D.items():
                    if v >= 4:
                        B[h][w] = k
                        B[h][-(w + 1)] = k
                        B[-(h + 1)][w] = k
                        B[-(h + 1)][-(w + 1)] = k
                        D[k] -= 4
                        break

        if H % 2 != 0:
            for w in range(W // 2):
                for k, v in D.items():
                    if v >= 2:
                        B[H // 2][w] = k
                        B[H // 2][-(w + 1)] = k
                        D[k] -= 2
                        break
        if W % 2 != 0:
            for h in range(H // 2):
                for k, v in D.items():
                    if v >= 2:
                        B[h][W // 2] = k
                        B[-(h + 1)][W // 2] = k
                        D[k] -= 2
                        break
        if H % 2 != 0 and W % 2 != 0:
            for k, v in D.items():
                if v >= 1:
                    B[H // 2][W // 2] = k
                    D[k] -= 1
                    break
    elif W == 1 and H > 1:
        for h in range(H // 2):
            for k, v in D.items():
                if v >= 2:
                    B[h][0] = k
                    B[-(h + 1)][0] = k
                    D[k] -= 2
                    break
        if H % 2 != 0:
            for k, v in D.items():
                if v >= 1:
                    B[H // 2][0] = k
                    D[k] -= 1
                    break
    elif H == 1 and W > 1:
        for w in range(W // 2):
            for k, v in D.items():
                if v >= 2:
                    B[0][w] = k
                    B[0][-(w + 1)] = k
                    D[k] -= 2
                    break
        if W % 2 != 0:
            for k, v in D.items():
                if v >= 1:
                    B[0][W // 2] = k
                    D[k] -= 1
                    break
    else:
        print("Yes")
        exit()

    for i in B:
        if "" in set(i):
            print("No")
            break
    else:
        print("Yes")


if __name__ == '__main__':
    resolve()
