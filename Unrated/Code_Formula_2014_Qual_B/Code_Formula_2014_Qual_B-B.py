# https://atcoder.jp/contests/code-formula-2014-qualb/submissions/13451969
# B - 11の倍数
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = input()[::-1]

    even, odd = 0, 0
    for i in range(len(n)):
        if i % 2 == 0:
            odd += int(n[i])
        else:
            even += int(n[i])

    print(even, odd)


if __name__ == '__main__':
    resolve()
