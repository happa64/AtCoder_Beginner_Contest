import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = 42
    while n <= 130000000:
        n += n
    print(n)


if __name__ == '__main__':
    resolve()
