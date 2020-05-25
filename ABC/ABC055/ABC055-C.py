import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())

    res = 0
    if 2 * n <= m:
        res += n
        m -= n * 2
        res += m // 4
    else:
        res += m // 2

    print(res)


if __name__ == '__main__':
    resolve()
