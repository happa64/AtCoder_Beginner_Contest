# https://atcoder.jp/contests/abc032/tasks/abc032_a
# A - 高橋君と青木君の好きな数
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a = int(input())
    b = int(input())
    n = int(input())

    for i in range(n, 10 ** 6):
        if i % a == 0 and i % b == 0:
            print(i)
            break


if __name__ == '__main__':
    resolve()
