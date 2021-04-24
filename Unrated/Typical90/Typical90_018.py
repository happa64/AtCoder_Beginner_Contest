import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    T = int(input())
    L, X, Y = map(int, input().split())
    Q = int(input())
    E = list(int(input()) for _ in range(Q))

    half = L / 2
    step = 360 / T
    for e in E:
        theta = step * e % 360
        h = 
        d =



if __name__ == '__main__':
    solve()
