# https://atcoder.jp/contests/joi2016yo/submissions/15096489
# B - ゼッケンの交換 (Swapping Bibs)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    Num = list(int(input()) for _ in range(n))

    for k in range(1, m + 1):
        for i in range(n - 1):
            if Num[i] % k > Num[i + 1] % k:
                Num[i], Num[i + 1] = Num[i + 1], Num[i]
    print(*Num, sep="\n")


if __name__ == '__main__':
    resolve()
