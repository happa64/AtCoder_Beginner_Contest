# https://atcoder.jp/contests/abc165/tasks/abc165_a
# A - We Love Golf
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    k = int(input())
    a, b = map(int, input().split())

    for i in range(a, b + 1):
        if i % k == 0:
            print("OK")
            break
    else:
        print("NG")


if __name__ == '__main__':
    resolve()
