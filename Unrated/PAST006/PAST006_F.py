# https://atcoder.jp/contests/past202104-open/submissions/22052148
# F - 安全装置
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n, l, t, x = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(n)]

    load_time = 0
    res = 0
    for a, b in AB:
        if b < l:
            res += a
            load_time = 0
        else:
            if a > t:
                print("forever")
                exit()
            while True:
                for _ in range(1, a + 1):
                    if load_time >= t:
                        load_time = 0
                        res += x
                        break
                    load_time += 1
                    res += 1
                else:
                    if load_time >= t:
                        load_time = 0
                        res += x
                    break
    print(res)


if __name__ == '__main__':
    solve()
