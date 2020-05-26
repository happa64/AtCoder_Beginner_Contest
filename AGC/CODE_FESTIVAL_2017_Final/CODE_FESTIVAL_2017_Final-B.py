# https://atcoder.jp/contests/cf17-final/submissions/13609114
# B - Palindrome-phobia
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()

    a = s.count("a")
    b = s.count("b")
    c = s.count("c")

    print("YES" if max(a, b, c) <= min(a, b, c) + 1 else "NO")


if __name__ == '__main__':
    resolve()
