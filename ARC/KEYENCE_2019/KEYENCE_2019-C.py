# https://atcoder.jp/contests/keyence2019/submissions/13655025
# C - Exam and Wizard
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    diff_AB = sum(A) - sum(B)

    if diff_AB < 0:
        print(-1)
        exit()

    Diff = []
    for i in range(n):
        Diff.append(A[i] - B[i])

    Diff.sort()

    res = 0
    for j in range(n):
        if Diff[j] < 0:
            res += 1
        else:
            if Diff[j] <= diff_AB:
                diff_AB -= Diff[j]
            else:
                diff_AB = 0
                res += 1

    if diff_AB > 0:
        res += 1

    print(res)


if __name__ == '__main__':
    resolve()
