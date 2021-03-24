# https://atcoder.jp/contests/arc115/submissions/21220516
# B - Plus Matrix
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())
    C = [list(map(int, input().split())) for _ in range(n)]

    A = [0] * n
    B = C[0]
    for i in range(n):
        A[i] = C[i][0] - B[0]

    mi = min(A)
    if mi < 0:
        A = [a - mi for a in A]
        B = [b + mi for b in B]

    if min(B) < 0:
        print("No")
        exit()

    for i in range(n):
        for j in range(n):
            if C[i][j] != A[i] + B[j]:
                print("No")
                exit()

    print("Yes")
    print(*A)
    print(*B)


if __name__ == '__main__':
    solve()
