import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())

    res = 0
    k = 5
    while n:
        n //= k
        res += 1
    print(res)


if __name__ == '__main__':
    resolve()
