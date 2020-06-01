# https://atcoder.jp/contests/abc169/submissions/13790680
# B - Multiplication 2
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = sorted(list(map(int, input().split())))

    res = 1
    for a in A:
        res *= a
        if res > 10 ** 18:
            print(-1)
            break
    else:
        print(res)


if __name__ == '__main__':
    resolve()
