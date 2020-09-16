# https://atcoder.jp/contests/abc116/submissions/13642855
# C - Grand Garden
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    H = list(map(int, input().split()))

    res = 0
    i = 0
    while sum(H) != 0:
        if H[i] != 0:
            while i < n and H[i] != 0:
                H[i] -= 1
                i += 1
            res += 1
            i = 0
        else:
            i += 1

    print(res)


if __name__ == '__main__':
    resolve()
