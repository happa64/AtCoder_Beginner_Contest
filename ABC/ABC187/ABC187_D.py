# https://atcoder.jp/contests/abc187/submissions/19134040
# D - Choose Me
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    AB = []
    A = T = 0
    for _ in range(n):
        a, b = map(int, input().split())
        AB.append([a + b + a, a, b])
        A += a
    AB.sort(key=lambda x: -x[0])

    for i in range(n):
        _, a, b = AB[i]
        A -= a
        T += a + b
        if A < T:
            print(i + 1)
            break


if __name__ == '__main__':
    resolve()
