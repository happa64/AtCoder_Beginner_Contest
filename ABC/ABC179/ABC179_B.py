# https://atcoder.jp/contests/abc179/submissions/16850890
# B - Go to Jail
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    cnt = 0
    for _ in range(n):
        d1, d2 = map(int, input().split())
        if d1 == d2:
            cnt += 1
        else:
            cnt = 0
        if cnt == 3:
            print("Yes")
            break
    else:
        print("No")


if __name__ == '__main__':
    resolve()
