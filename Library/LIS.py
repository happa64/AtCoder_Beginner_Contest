# 配列Lの最長増加部分列を求める
import bisect

LIS = [L[0]]
    for i in range(n):
        if L[i] > LIS[-1]:
            LIS.append(L[i])
        else:
            idx = bisect.bisect_left(LIS, L[i])
            LIS[idx] = L[i]
