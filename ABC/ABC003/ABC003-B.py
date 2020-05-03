# https://atcoder.jp/contests/abc003/tasks/abc003_2
# B - AtCoderトランプ
import sys

sys.setrecursionlimit(10 ** 7)


def resolve():
    s = input()
    t = input()
    L = ["a", "t", "c", "o", "d", "e", "r"]

    for i, j in zip(s, t):
        if i != j:
            if i in L and j == "@":
                continue
            elif i == "@" and j in L:
                continue
            else:
                print("You will lose")
                exit()
    else:
        print("You can win")


if __name__ == '__main__':
    resolve()
