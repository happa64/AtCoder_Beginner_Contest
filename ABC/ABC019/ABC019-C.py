# https://atcoder.jp/contests/abc019/submissions/13472930
# C - 高橋くんと魔法の箱
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = sorted(list(map(int, input().split())))

    B = set()
    for a in A:
        while a % 2 == 0:
            a //= 2
        B.add(a)

    print(len(B))


if __name__ == '__main__':
    resolve()
