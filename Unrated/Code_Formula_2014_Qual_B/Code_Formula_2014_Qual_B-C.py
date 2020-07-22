# https://atcoder.jp/contests/code-formula-2014-qualb/submissions/15360700
# C - 仲良し文字列
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    A = list(input())
    B = list(input())
    n = len(A)

    if sorted(A) != sorted(B):
        print("NO")
        exit()

    cnt = 3
    for i in range(n):
        if A[i] != B[i]:
            if cnt:
                for j in range(n):
                    if A[i] == B[j] and A[j] == B[i]:
                        B[i], B[j] = B[j], B[i]
                        cnt -= 1
                        break
                else:
                    for j in range(n):
                        if A[i] == B[j] and A[j] != B[j]:
                            B[i], B[j] = B[j], B[i]
                            cnt -= 1
                            break

    if A != B:
        print("NO")
    else:
        if cnt % 2 == 0:
            print("YES")
        else:
            print("YES" if len(A) != len(set(A)) else "NO")


if __name__ == '__main__':
    resolve()
