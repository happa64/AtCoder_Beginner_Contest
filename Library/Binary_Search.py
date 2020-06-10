def meguru_bisect(ok, ng):
    """
    is_okを定義して下さい
    :param ok: 取りうる最小の値-1
    :param ng: 取りうる最大の値+1
    :return: is_okを満たす最小(もしくは最大)の値
    """
    while abs(ok - ng) > 0:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


def ternary_search(high, low):
    """
    f=凸関数の式
    :param high:取りうる一番大きい値
    :param low:取りうる一番小さい値
    :return: 凸関数の極小値（極大値）
    """
    while abs(high - low) > 10 ** (-9):
        mid_left = high / 3 + low * 2 / 3
        mid_right = high * 2 / 3 + low / 3
        if f(mid_left) >= f(mid_right):
            low = mid_left
        else:
            high = mid_right
    return f(high)