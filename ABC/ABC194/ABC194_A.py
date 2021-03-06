# https://atcoder.jp/contests/abc194/submissions/20691047
# A - I Scream
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    a, b = map(int, input().split())
    ab = a + b

    if ab >= 15 and b >= 8:
        print(1)
    elif ab >= 10 and b >= 3:
        print(2)
    elif ab >= 3:
        print(3)
    else:
        print(4)


if __name__ == '__main__':
    solve()
