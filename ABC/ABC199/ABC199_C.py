import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())
    S = input()
    q = int(input())

    T = deque([list(S[:n]), list(S[n:])])

    for _ in range(q):
        t, a, b = map(lambda x: int(x) - 1, input().split())
        if t == 0:
            i, a = divmod(a, n)
            j, b = divmod(b, n)
            tmp = T[i][a]
            T[i][a] = T[j][b]
            T[j][b] = tmp
        else:
            t = T.popleft()
            T.append(t)

    res = "".join(T[0]) + "".join(T[1])
    print(res)


if __name__ == '__main__':
    solve()
