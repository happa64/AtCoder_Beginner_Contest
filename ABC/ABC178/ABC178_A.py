# https://atcoder.jp/contests/abc178/submissions/16669503
# A - Not
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x = int(input())
    print(1 if x == 0 else 0)



if __name__ == '__main__':
    resolve()
