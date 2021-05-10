# https://codeforces.com/contest/1455/submission/100037831
# D - Sequence and Swaps
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        A = [-f_inf] + list(map(int, input().split())) + [f_inf]

        res = 0
        while True:
            for i in range(n + 1):
                if A[i] > A[i + 1]:
                    break
            else:
                break
            for i in range(n + 1):
                if A[i] > x:
                    tmp = A[i]
                    A[i] = x
                    x = tmp
                    res += 1
                    break
            else:
                res = -1
                break
        print(res)


if __name__ == '__main__':
    resolve()
