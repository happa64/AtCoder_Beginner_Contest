# https://atcoder.jp/contests/abc047/submissions/14206477
# A - キャンディーと2人の子供
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b, c = map(int, input().split())
    if a + b == c or b + c == a or c + a == b:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    resolve()
