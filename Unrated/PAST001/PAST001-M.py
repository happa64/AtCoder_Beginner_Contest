import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(n)]
    CD = [list(map(int, input().split())) for _ in range(m)]
    # 選んだ集合の強さx = sum(b) // sum(a) を最大化したい
    # xを二分探索して考える

    # 強さxを達成することが可能か判定する
    # x <= sum(b) // sum(a)を変形し、sum(b) - x * sum(a) >= 0とななればよい
    def is_ok(x):
        ab = []
        for i in range(n):
            a, b = AB[i]
            ab.append(b - x * a)
        ab = sorted(ab, reverse=True)
        # max_ab:お助けモンスターを使わない場合
        max_ab = sum(ab[:5])

        cd = []
        for i in range(m):
            c, d = CD[i]
            cd.append(d - x * c)
        cd = sorted(cd, reverse=True)
        # max_abcd:お助けモンスターを使う場合
        max_abcd = sum(ab[:4]) + cd[0]

        res = max(max_ab, max_abcd)
        return res >= 0

    # 二分探索
    def meguru_bisect(ng, ok):
        while abs(ok - ng) > 10 ** (-7):
            mid = (ok + ng) / 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    print(meguru_bisect(10 ** 9 + 1, 0))


if __name__ == '__main__':
    resolve()
