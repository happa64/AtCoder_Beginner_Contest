# https://atcoder.jp/contests/abc185/submissions/18735060
# D - Stamp
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    if m == 0:
        print(1)
        exit()

    A = list(map(int, input().split()))
    A.sort()

    prev = 0
    sec = []
    for i in range(m):
        diff = A[i] - prev - 1
        if diff:
            sec.append(diff)
        prev = A[i]
    diff = n - prev
    if diff:
        sec.append(n - prev)

    if not sec:
        print(0)
        exit()

    k = min(sec)
    res = 0
    for s in sec:
        res += (s + k - 1) // k
    print(res)


if __name__ == '__main__':
    resolve()
