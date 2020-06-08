# https://atcoder.jp/contests/abc105/submissions/14117688
# C - Base -2 Number
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    if n == 0:
        print(0)
        exit()
    bit = []
    i = 0
    base = 1
    while n != 0:
        if n % (base * 2) == 0:
            bit.append("0")
        else:
            bit.append("1")
            n -= base
        i += 1
        base *= -2
    print("".join(bit[::-1]))


if __name__ == '__main__':
    resolve()
