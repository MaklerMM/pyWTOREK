def geometric (n, a0 = 1, q = 2):
        return a0 * ((1 - pow(q,n))/(1 - q)), a0 * pow(q, n-1)

print("%10s %10s" % ("suma_elem", "last_elem"))
print("%10d %10d" % geometric(3, a0=3))
print("%10d %10d" % geometric(4, a0=3))
print("%10d %10d" % geometric(5, a0=3))
print("%10d %10d" % geometric(6, a0=3))

