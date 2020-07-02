# https://atcoder.jp/contests/abc156/submissions/13642227
# A - Beginner
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, r = map(int, input().split())
    diff = 100 * (max(0, 10 - n))
    print(r + diff)

if __name__ == '__main__':
    resolve()
