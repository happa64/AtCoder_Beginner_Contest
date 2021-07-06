# https://atcoder.jp/contests/typical90/submissions/24011713
# 084 - There are two types of characters（★3）
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())
    S = input().rstrip()

    o, x = deque([]), deque([])
    for i in range(n):
        o.append(i) if S[i] == "o" else x.append(i)

    res = 0
    for i in range(n):
        if S[i] == "o":
            while x and x[0] < i:
                x.popleft()
            if x:
                res += n - x[0]
        else:
            while o and o[0] < i:
                o.popleft()
            if o:
                res += n - o[0]
    print(res)


if __name__ == '__main__':
    solve()
