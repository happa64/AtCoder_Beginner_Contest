# https://atcoder.jp/contests/abc004/tasks/abc004_2
# B - 回転
import sys

sys.setrecursionlimit(10 ** 7)


def resolve():
    C = [list(map(str, input().split())) for _ in range(4)]
    for res in C[::-1]:
        print(*res[::-1])


if __name__ == '__main__':
    resolve()
