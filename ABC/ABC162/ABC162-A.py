# https://atcoder.jp/contests/abc162/tasks/abc162_a
# A - Lucky 7
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = input()

    for i in n:
        if i == "7":
            print("Yes")
            exit()
    print("No")


if __name__ == '__main__':
    resolve()
