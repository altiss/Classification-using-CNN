def method():
    a, b = 1, 2
    c, d = 3, 4
    e = a + b
    f = a + b + e - c
    g = a + c + e + f
    return a + b + c - d - e - f + g
