# https://atcoder.jp/contests/abc136/submissions/13404754
# C - Build Stairs
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    H = list(map(int, input().split()))

    for i in range(1, n):
        if H[i - 1] < H[i]:
            H[i] -= 1

    for j in range(1, n):
        if H[j - 1] > H[j]:
            print("No")
            break
    else:
        print("Yes")


if __name__ == '__main__':
    resolve()
