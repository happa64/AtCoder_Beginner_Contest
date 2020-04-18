# https://atcoder.jp/contests/abc009/tasks/abc009_2
# B - 心配性な富豪、ファミリーレストランに行く。
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = sorted(list(int(input()) for _ in range(n)), reverse=True)

    for i in range(1, n):
        if A[i - 1] != A[i]:
            print(A[i])
            break


if __name__ == '__main__':
    resolve()
