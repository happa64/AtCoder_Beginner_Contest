# https://atcoder.jp/contests/ddcc2020-final/submissions/17100014
# A - Div/de
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    res = 0
    for a in A:
        cnt = 0
        while a != 1:
            for i in range(2, a + 1):
                if a % i == 0:
                    a //= i
                    cnt += 1
                    break
        res ^= cnt
    print("Yes" if res else "No")


if __name__ == '__main__':
    resolve()
