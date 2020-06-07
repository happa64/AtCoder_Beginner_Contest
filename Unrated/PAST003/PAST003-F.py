# https://atcoder.jp/contests/past202005-open/submissions/14079420
# F - 回文行列
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7
STR = [chr(i).lower() for i in range(97, 97 + 26)]


def resolve():
    n = int(input())
    A = [list(input()) for _ in range(n)]

    L = [[0] * 26 for _ in range(n)]
    for i in range(n):
        for j in range(n):
            idx = STR.index(A[i][j])
            L[i][idx] = 1

    res = [""] * n
    for i in range(n // 2):
        for j in range(26):
            if L[i][j] and L[-(i + 1)][j]:
                res[i] = res[-(i + 1)] = STR[j]
                break
        else:
            print(-1)
            break
    else:
        if n % 2:
            for j in range(26):
                if L[n // 2][j]:
                    res[n // 2] = STR[j]

        res = "".join(res)
        print(res)


if __name__ == '__main__':
    resolve()
