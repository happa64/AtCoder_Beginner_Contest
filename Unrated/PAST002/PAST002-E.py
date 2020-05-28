# https://atcoder.jp/contests/past202004-open/tasks/past202004_e
# E - 順列
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    res = []
    for i in range(n):
        cnt = 1
        j = i
        while i + 1 != A[j]:
            j = A[j] - 1
            cnt += 1
        res.append(cnt)
    print(*res)


if __name__ == '__main__':
    resolve()
