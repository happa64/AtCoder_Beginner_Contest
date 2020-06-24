# https://atcoder.jp/contests/chokudai_S001/submissions/14660839
# I - 和がNの区間
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    res = 0
    left = 0
    total = 0
    for right in range(n):
        total += A[right]
        while total > n:
            total -= A[left]
            left += 1
        if total == n:
            res += 1

    print(res)


if __name__ == '__main__':
    resolve()
