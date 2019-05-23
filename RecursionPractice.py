def f(n):
    print('\tn =', n)
    if n == 1:
        print('Returning...')
        print('\tn =', n, 'return:', 1)
        return 1
    else:
        r = n * f(n - 1)
        print('\tn =', n, 'return:', r)
        return r


print('Call f(5)...')
print('Get out of f(n), and f(5) =', f(5))