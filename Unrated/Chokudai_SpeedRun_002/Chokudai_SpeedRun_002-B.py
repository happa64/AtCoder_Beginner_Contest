# https://atcoder.jp/contests/chokudai_S002/submissions/15394648
# B - あまり α
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        print(a % b)


if __name__ == '__main__':
    resolve()
