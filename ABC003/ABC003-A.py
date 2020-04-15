# https://atcoder.jp/contests/abc003/tasks/abc003_1
# A - AtCoder社の給料
import sys

sys.setrecursionlimit(10 ** 7)


def resolve():
    n = int(input())

    res = 0
    for i in range(1, n + 1):
        res += i * 10000 / n
    print(int(res))


if __name__ == '__main__':
    resolve()
