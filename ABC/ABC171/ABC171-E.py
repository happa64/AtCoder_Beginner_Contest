# https://atcoder.jp/contests/abc171/submissions/14690601
# E - Red Scarf
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    flg = ["0"] * 40
    for i in range(40):
        cnt = 0
        for a in A:
            if (a >> i) & 1:
                cnt += 1
        if cnt % 2 != 0:
            flg[i] = "1"

    flg = int("".join(flg[::-1]), 2)
    res = [a ^ flg for a in A]
    print(*res)


if __name__ == '__main__':
    resolve()
