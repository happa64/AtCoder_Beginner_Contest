# https://atcoder.jp/contests/abc004/tasks/abc004_3
# C - 入れ替え
import sys

sys.setrecursionlimit(10 ** 7)


def resolve():
    n = int(input())
    L = ["1", "2", "3", "4", "5", "6"]
    for i in range(n % 30):
        L[i % 5], L[i % 5 + 1] = L[i % 5 + 1], L[i % 5]

    print("".join(L))


if __name__ == '__main__':
    resolve()
