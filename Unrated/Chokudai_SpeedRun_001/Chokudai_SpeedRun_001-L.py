# https://atcoder.jp/contests/chokudai_S001/submissions/14669968
# L - N回スワップ
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    cnt = 0
    for i in range(n):
        while A[i] != i + 1:
            A[A[i] - 1], A[i] = A[i], A[A[i] - 1]
            cnt += 1
    print("YES" if n % 2 == cnt % 2 else "NO")


if __name__ == '__main__':
    resolve()
