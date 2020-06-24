# https://atcoder.jp/contests/arc038/submissions/14646805
# A - カードと兄妹
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = sorted(list(map(int, input().split())), reverse=True)

    tot = 0
    for i in range(n):
        if i % 2 == 0:
            tot += A[i]
    print(tot)


if __name__ == '__main__':
    resolve()
