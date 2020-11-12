# https://atcoder.jp/contests/abc104/submissions/13577288
# C - All Green
import sys
from itertools import product

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    d, g = map(int, input().split())
    PC = []
    for i in range(d):
        p, c = map(int, input().split())
        PC.append([(i + 1) * 100, p, c])

    res = f_inf
    # 全完する難易度を1、それ以外の難易度を0としてbit全探索する
    for pattern in product([0, 1], repeat=d):
        score = 0
        cnt = 0
        remain = []
        for idx, p in enumerate(pattern):
            if p == 1:
                point, num, bonus = PC[idx]
                score += point * num + bonus
                cnt += num
            else:
                remain.append(PC[idx])

        # もし全完した難易度だけでG以上のスコアが出ればOK
        if score >= g:
            res = min(res, cnt)
        # G以上のスコアが出なければ、G以上になるまで、全完しなかった難易度を難易度の高い順に”全完しないよう”に解いていく
        else:
            remain = sorted(remain, key=lambda x: x[0], reverse=True)
            diff = g - score
            for point, num, bonus in remain:
                if diff <= point * (num - 1):
                    cnt += diff // point + (1 if diff % point else 0)
                    res = min(res, cnt)
                    break
                else:
                    cnt += num - 1
                    score += point * (num - 1)

    print(res)


if __name__ == '__main__':
    resolve()
