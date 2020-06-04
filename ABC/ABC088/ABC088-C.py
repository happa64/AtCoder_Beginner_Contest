# https://atcoder.jp/contests/abc088/submissions/13231076
# C - Takahashi's Information
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    C = [list(map(int, input().split())) for _ in range(n)]

    a = [f_inf] * 3
    b = [f_inf] * 3

    # a1を0に決め打ちしすると、Cの一行目と一列目からa1~3とb1~3が定まる
    a[0] = 0
    for j in range(3):
        b[j] = C[0][j] - a[0]

    for i in range(3):
        a[i] = C[i][0] - b[0]

    # a1~3とb1~3がCと矛盾しないか調査
    for i in range(3):
        for j in range(3):
            if C[i][j] != a[i] + b[j]:
                print("No")
                exit()

    print("Yes")


if __name__ == '__main__':
    resolve()
