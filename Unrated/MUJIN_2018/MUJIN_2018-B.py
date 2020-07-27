# https://atcoder.jp/contests/mujin-pc-2018/submissions/15490343
# B - セキュリティ
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    A = int(input())
    S = input()
    n = len(S)

    if A == 0:
        print("Yes")
        exit()

    for i in range(n):
        if S[i] == "+":
            A += 1
        else:
            A -= 1
        if A == 0:
            print("Yes")
            exit()
    print("No")


if __name__ == '__main__':
    resolve()
