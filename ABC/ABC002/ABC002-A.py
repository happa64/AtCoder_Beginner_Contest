# https://atcoder.jp/contests/abc002/tasks/abc002_1
# A - 正直者
import sys

sys.setrecursionlimit(10 ** 7)


def resolve():
    x, y = map(int, input().split())
    print(max(x, y))


if __name__ == '__main__':
    resolve()
