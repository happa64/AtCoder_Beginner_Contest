import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    for i in range(k, n):
        prev = A[i - k]
        now = A[i]
        print("Yes" if prev < now else "No")


if __name__ == '__main__':
    resolve()
