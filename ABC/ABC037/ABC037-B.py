# https://atcoder.jp/contests/abc037/submissions/14015127
# B - 編集
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, q = map(int, input().split())
    A = [0] * n
    for _ in range(q):
        l, r, t = map(int, input().split())
        for i in range(l - 1, r):
            A[i] = t
    print(*A, sep="\n")


if __name__ == '__main__':
    resolve()
