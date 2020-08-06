# https://atcoder.jp/contests/nikkei2019-ex/submissions/15724538
# C - 11で割った余りの計算方法
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    print(n % 11)


if __name__ == '__main__':
    resolve()
