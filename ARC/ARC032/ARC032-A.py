# https://atcoder.jp/contests/arc032/submissions/14638839
# A - ホリドッグ
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    N = int(input())
    su = (N + 1) * N // 2

    if su == 1:
        print("BOWWOW")
        exit()

    for i in range(2, int(pow(su, 0.5)) + 1):
        if su % i == 0:
            print("BOWWOW")
            break
    else:
        print("WANWAN")


if __name__ == '__main__':
    resolve()
