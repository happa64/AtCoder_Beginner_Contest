import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def resolve():
    n, k = map(int, input().split())
    A = sorted(list(map(int, input().split())))

    if k in set(A):
        print("POSSIBLE")
        exit()

    if k > A[-1]:
        print("IMPOSSIBLE")
        exit()

    if n == 1:
        print("IMPOSSIBLE")
        exit()

    g = A[0]
    for i in range(1, n):
        g = gcd(g, A[i])

    if k % g == 0:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")


if __name__ == '__main__':
    resolve()
