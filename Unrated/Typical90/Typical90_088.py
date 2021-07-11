# https://atcoder.jp/contests/typical90/submissions/24165049
# 088 - Similar but Different Ways（★6）
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    def dfs(i, choice, tot):
        if i == n:
            return
        dfs(i + 1, choice, tot)
        for x in choice:
            if (x, i + 1) in XY:
                break
        else:
            choice.append(i + 1)
            tot += A[i]
            if not dup[tot]:
                dup[tot].append(tuple(choice))
                dfs(i + 1, choice, tot)
                choice.pop()
                tot -= A[i]
            else:
                res1 = choice
                res2 = dup[tot][0]
                print(len(res1))
                print(*res1)
                print(len(res2))
                print(*res2)
                exit()

    n, q = map(int, input().split())
    A = tuple(map(int, input().split()))
    MAX = sum(A)
    XY = set(tuple(map(int, input().split())) for _ in range(q))
    dup = [[] for _ in range(MAX + 1)]
    dfs(0, [], 0)


if __name__ == '__main__':
    solve()
