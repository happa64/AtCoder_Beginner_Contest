import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    m, d = map(int, input().split())

    res = 0
    for i in range(4, m + 1):
        for j in range(22, d + 1):
            d1, d10 = divmod(j, 10)
            if i == d1 * d10 and d1 >= 2 and d10 >= 2:
                res += 1

    print(res)


if __name__ == '__main__':
    resolve()
