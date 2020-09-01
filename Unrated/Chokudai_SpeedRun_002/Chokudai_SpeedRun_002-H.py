import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        if a == b:
            print(-1)
        else:
            print(abs(a - b))


if __name__ == '__main__':
    resolve()
