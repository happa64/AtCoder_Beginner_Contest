# https://atcoder.jp/contests/abc212/submissions/24651289
# B - Weak Password
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    X = input()
    if len(set(X)) == 1:
        print("Weak")
    else:
        x = int(X[0])
        flg = True
        for i in range(1, 4):
            if (x + 1) % 10 != int(X[i]):
                flg = False
                break
            else:
                x = int(X[i])
        if flg:
            print("Weak")
        else:
            print("Strong")


if __name__ == '__main__':
    solve()
