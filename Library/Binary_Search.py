def meguru_bisect(ok, ng):
    """
    is_okを定義して下さい
    :param ok: 取りうる最小の値-1
    :param ng: 取りうる最大の値+1
    :return: is_okを満たす最小(もしくは最大)の値
    """
    while abs(ok - ng) > 10 ** (-7):
        mid = (ok + ng) / 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok