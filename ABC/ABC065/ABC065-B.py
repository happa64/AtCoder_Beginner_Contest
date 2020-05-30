# https://atcoder.jp/contests/abc065/submissions/12897360
# B - Trained?
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(int(input()) for _ in range(n))

    j = 1
    cnt = 0
    for i in range(n):
        if j == 2:
            break
        j = A[j - 1]
        cnt += 1
    else:
        print(-1)
        exit()

    print(cnt)


if __name__ == '__main__':
    resolve()
