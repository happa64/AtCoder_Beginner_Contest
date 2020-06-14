# https://atcoder.jp/contests/arc019/submissions/14270400
# B - こだわりの名前
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    A = input()
    n = len(A)

    cnt = 0 if n % 2 == 0 else 1
    for i in range(n // 2):
        if A[i] == A[-(i + 1)]:
            cnt += 2

    if cnt == n:
        if n % 2 != 0:
            res = 25 * (n - 1)
        else:
            res = 25 * n
    else:
        if (n - cnt) // 2 == 1:
            res = 25 * n - (n - cnt)
        else:
            res = 25 * n

    print(res)


if __name__ == '__main__':
    resolve()
