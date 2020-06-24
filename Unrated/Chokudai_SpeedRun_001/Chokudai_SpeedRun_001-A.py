# https://atcoder.jp/contests/chokudai_S001/submissions/14660390
# A - 最大値
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    print(max(A))


if __name__ == '__main__':
    resolve()
