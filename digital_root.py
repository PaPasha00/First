def digital_root(n):
    if n // 10 == 0:
        return n
    else:
        m = 0
        while n > 0:
            m += n % 10
            n = n // 10
    if m // 10 == 0:
        return m
    else:
        return digital_root(m)
