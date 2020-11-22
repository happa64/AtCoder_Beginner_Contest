import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    for i in range(n - 7, n + 1):
        print(i)


if __name__ == '__main__':
    resolve()
