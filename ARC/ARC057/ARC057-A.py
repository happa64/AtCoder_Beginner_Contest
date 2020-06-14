# https://atcoder.jp/contests/arc057/submissions/14267352
# A - 2兆円
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, k = map(int, input().split())
    if k == 0:
        print(2 * pow(10, 12) - a)
        exit()

    total = a
    for i in range(1, 10 ** 6):
        total += 1 + k * total
        if total >= 2 * pow(10, 12):
            print(i)
            break


if __name__ == '__main__':
    resolve()
