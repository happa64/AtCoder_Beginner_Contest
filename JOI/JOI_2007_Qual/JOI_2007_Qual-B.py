import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    check = [False] * 30
    for _ in range(28):
        n = int(input())
        check[n - 1] = True

    res = []
    for i in range(30):
        if not check[i]:
            res.append(i + 1)
    print(*res, sep="\n")


if __name__ == '__main__':
    resolve()
