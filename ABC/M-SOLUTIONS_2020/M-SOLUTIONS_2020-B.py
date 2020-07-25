import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b, c = map(int, input().split())
    k = int(input())

    while k and a >= b:
        b *= 2
        k -= 1

    while k and b >= c:
        c *= 2
        k -= 1

    print("Yes" if a < b < c else "No")


if __name__ == '__main__':
    resolve()
