# https://atcoder.jp/contests/arc103/submissions/19517661
# E - Tr/ee
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = list(input().rstrip())
    n = len(s)

    if s[0] == "0" or s[-1] == "1":
        print(-1)
        exit()

    for i in range(n):
        if s[i] != s[n - i - 2]:
            print(-1)
            exit()

    s[-1] = "1"
    prev = n
    for i in reversed(range(n - 1)):
        print(prev, i + 1)
        if s[i] == "1":
            prev = i + 1


if __name__ == '__main__':
    resolve()
