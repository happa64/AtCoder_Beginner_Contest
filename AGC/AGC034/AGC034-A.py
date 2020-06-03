# https://atcoder.jp/contests/agc034/tasks/agc034_a
# A - Kenken Race
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, a, b, c, d = map(int, input().split())
    s = input()

    flg = False
    for i in range(a, d):
        # 2マス連続で岩が置いてある場合は不可能である
        if s[i] == "#":
            if s[i + 1] == "#":
                print("No")
                break

        # Bの1マス前から、Dマスまでの間に3つ連続で何も置かれていないマスがあればフラグを立てる
        if b - 1 <= i:
            if i + 1 < n:
                if s[i - 1] == s[i] == s[i + 1] == ".":
                    flg = True
    else:
        # CよりDが後ろにあれば可能である
        if c < d:
            print("Yes")
        else:
            # DよりCが後ろにあり、かつフラグが立っていれば可能である
            if flg:
                print("Yes")
            else:
                print("No")


if __name__ == '__main__':
    resolve()
