# https://atcoder.jp/contests/tenka1-2018-beginner/submissions/15305630
# D - Crossing
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    N = n * 2
    for i in range(1, int(pow(N, 0.5)) + 1):
        if N % i == 0 and abs(N // i - i) == 1:
            x, y = i, N // i
            print("Yes")
            print(y)
            break
    else:
        print("No")
        exit()

    res = [[0] * x for _ in range(y)]
    num = 1
    left = 0
    while left < y:
        for i in range(left, x):
            res[left][i] = num
            res[i + 1][left] = num
            num += 1
        left += 1

    for i in res:
        print(x, *i)


if __name__ == '__main__':
    resolve()
