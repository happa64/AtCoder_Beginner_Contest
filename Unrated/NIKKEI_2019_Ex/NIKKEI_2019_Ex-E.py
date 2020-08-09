# https://atcoder.jp/contests/nikkei2019-ex/submissions/15791792
# E - スーパーFizzBuzz
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())

    for i in range(1, n + 1):
        res = ""
        if i % 2 == 0:
            res += "a"
        if i % 3 == 0:
            res += "b"
        if i % 4 == 0:
            res += "c"
        if i % 5 == 0:
            res += "d"
        if i % 6 == 0:
            res += "e"
        print(i if res == "" else res)


if __name__ == '__main__':
    resolve()
