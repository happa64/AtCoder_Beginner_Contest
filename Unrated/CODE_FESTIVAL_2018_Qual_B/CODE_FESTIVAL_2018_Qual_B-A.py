# https://atcoder.jp/contests/code-festival-2018-qualb/submissions/15390201
# A - Probability of Participation
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    res = 100 - 100 // n
    print(res)


if __name__ == '__main__':
    resolve()
