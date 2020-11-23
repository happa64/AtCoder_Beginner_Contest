# https://atcoder.jp/contests/iroha2019-day1/submissions/18372041
# H - ちらし寿司
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    N = input().rstrip()
    tot = sum([int(n) for n in N])
    l = (tot + 8) // 9
    if (len(set(N)) == 1 and "9" in set(N)) or len(N) == 1:
        l += 1
    res = [1] * l
    tot -= l
    i = 0
    while tot:
        if tot > 8:
            tot -= 8
            res[i] += 8
        else:
            res[i] += tot
            tot = 0
        i += 1
    res = res[::-1]
    ans = "".join(map(str, res))
    if ans == N:
        res[0] = str(int(res[0]) + 1)
        res[1] = str(int(res[1]) - 1)
        ans = "".join(map(str, res))
    print(ans)


if __name__ == '__main__':
    resolve()
