# https://atcoder.jp/contests/abc054/submissions/12215743
# B - Template Matching
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    A = [list(input()) for _ in range(n)]
    B = [list(input()) for _ in range(m)]

    for i in range(n - m + 1):
        for j in range(n - m + 1):
            for k in range(m):
                for l in range(m):
                    if A[i + k][j + l] != B[k][l]:
                        break
                else:
                    continue
                break
            else:
                print("Yes")
                exit()
    else:
        print("No")


if __name__ == '__main__':
    resolve()
