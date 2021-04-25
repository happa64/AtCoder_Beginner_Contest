# https://atcoder.jp/contests/past202104-open/submissions/22052074
# A - POSTal Code
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    S = input()

    flg = True
    for i in range(8):
        if i == 3:
            if S[3] != "-":
                flg = False
                break
        else:
            if not S[i].isdigit():
                flg = False
                break

    print("Yes" if flg else "No")


if __name__ == '__main__':
    solve()
