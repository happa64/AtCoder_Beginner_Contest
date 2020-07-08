# https://atcoder.jp/contests/joi2013yo/submissions/15076440
# C - 看板 (Signboard)
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def dfs(v):
        if v == l:
            tmp.append(nums[::])
            return

        for u in idx[v]:
            if v != 0:
                if u <= nums[v - 1]:
                    continue
            nums[v] = u
            dfs(v + 1)

    n = int(input())
    g = input()
    l = len(g)
    S = list(input() for _ in range(n))

    res = 0
    for s in S:
        idx = [[] for _ in range(l)]
        for i in range(l):
            for j in range(len(s)):
                if g[i] == s[j]:
                    idx[i].append(j)

        nums = [0] * l
        tmp = []
        dfs(0)
        for nums in tmp:
            dist = nums[1] - nums[0]
            for i in range(2, l):
                if nums[i] - nums[i - 1] != dist:
                    break
            else:
                res += 1
                break
    print(res)


if __name__ == '__main__':
    resolve()
