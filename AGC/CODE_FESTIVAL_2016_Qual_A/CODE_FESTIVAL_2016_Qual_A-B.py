# https://atcoder.jp/contests/code-festival-2016-quala/tasks/codefestival_2016_qualA_b
# B - 仲良しうさぎ
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    res = 0
    for i in range(n):
        if A[A[i] - 1] == i + 1:
            res += 1

    print(res // 2)


if __name__ == '__main__':
    resolve()
