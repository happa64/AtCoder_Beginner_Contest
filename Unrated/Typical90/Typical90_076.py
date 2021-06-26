# https://atcoder.jp/contests/typical90/submissions/23739216
# 076 - Cake Cut（★3）
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())
    A = tuple(map(int, input().split()))

    target = sum(A)
    now = 0
    left = right = 0
    while left < n:
        while now < target:
            now += A[right] * 10
            if now == target:
                print("Yes")
                exit()
            right = (right + 1) % n
        now -= A[left] * 10
        left += 1
    print("No")


if __name__ == '__main__':
    solve()
