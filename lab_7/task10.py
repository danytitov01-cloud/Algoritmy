def count_depth(n):
    if n == 0:
        return 1
    return 1 + count_depth(n - 1)