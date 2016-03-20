def fermat_test(n, k=100):
    if n == 2 : return True
    if n < 2 or n & 1 == 0 : return False
    for i in range(2, k) :
        x, y = n, i
        while y :
            x, y = y, x % y
        if x != 1 : continue
        if pow(i, n-1, n) != 1 :
            return False
    return True

