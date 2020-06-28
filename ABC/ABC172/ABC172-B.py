# https://atcoder.jp/contests/abc172/submissions/14777835
# B - Minor Change
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S = input()
    T = input()
    res = 0
    for s, t in zip(S, T):
        if s != t:
            res += 1
    print(res)


if __name__ == '__main__':
    resolve()
