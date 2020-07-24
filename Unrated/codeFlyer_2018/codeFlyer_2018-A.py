# https://atcoder.jp/contests/bitflyer2018-qual/submissions/15395070
# A - 本選参加者数
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a = int(input())
    b = int(input())

    res = 0
    for i in range(a + 1):
        if i % b == 0:
            res = i
    print(res)


if __name__ == '__main__':
    resolve()
