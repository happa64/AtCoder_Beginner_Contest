# https://codingcompetitions.withgoogle.com/codejam/round/00000000004330f6/0000000000432f33
# Minimum Scalar Product
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    t = int(input())
    for i in range(1, t + 1):
        n = int(input())
        v1 = list(map(int, input().split()))
        v2 = list(map(int, input().split()))

        v1.sort()
        v2.sort(reverse=True)

        res = sum(v1[i] * v2[i] for i in range(n))
        print("Case #{}: {}".format(i, res))


if __name__ == '__main__':
    resolve()
