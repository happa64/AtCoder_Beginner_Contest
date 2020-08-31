# https://atcoder.jp/contests/agc029/submissions/16423823
# B - Powers of two
import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    MAX = A[-1] * 2
    D = Counter(A)
    res = 0
    for i in reversed(range(n)):
        if D[A[i]] == 0:
            continue
        target = 2
        while target <= MAX:
            if D.get(target - A[i], 0) != 0:
                if A[i] != target - A[i]:
                    D[A[i]] -= 1
                    D[target - A[i]] -= 1
                    res += 1
                    break
                else:
                    if D[A[i]] != 1:
                        D[A[i]] -= 2
                        res += 1
                        break
            target *= 2
    print(res)


if __name__ == '__main__':
    resolve()
