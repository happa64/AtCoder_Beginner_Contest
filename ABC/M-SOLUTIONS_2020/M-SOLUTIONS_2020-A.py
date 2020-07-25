import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x = int(input())
    res = 8 - (x - 400) // 200
    print(res)

if __name__ == '__main__':
    resolve()
