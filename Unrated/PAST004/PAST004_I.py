# https://atcoder.jp/contests/past202010-open/submissions/18010728
# I - ピザ
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    total = sum(A)
    x = 0
    y = total
    right = 0
    res = f_inf
    for left in range(n):
        while x < y:
            x += A[right]
            y -= A[right]
            diff = abs(x - y)
            res = min(res, diff)
            right += 1
            if right == n:
                right = 0
        x -= A[left]
        y += A[left]
        diff = abs(x - y)
        res = min(res, diff)
    print(res)


if __name__ == '__main__':
    resolve()
