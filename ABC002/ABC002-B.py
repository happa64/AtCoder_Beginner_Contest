# https://atcoder.jp/contests/abc002/tasks/abc002_2
# B - 罠
import sys

sys.setrecursionlimit(10 ** 7)


def resolve():
    w = input()
    res = []
    for s in w:
        if s not in ["a", "i", "u", "e", "o"]:
            res.append(s)
    print("".join(res))


if __name__ == '__main__':
    resolve()
