# https://atcoder.jp/contests/abc067/submissions/13979345
# A - Sharing Cookies
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b = map(int, input().split())
    print("Possible" if (a + b) % 3 == 0 or a % 3 == 0 or b % 3 == 0 else "Impossible")


if __name__ == '__main__':
    resolve()
