from ctypes import cdll, c_int, c_float, POINTER
libalex = cdll.LoadLibrary('./libalex.so')


libalex.exponent.argtypes = (c_int, c_float)
libalex.exponent.restype = c_float

def alex_exponent(n, f):
    return libalex.exponent(c_int(n), c_float(f))


libalex.sum.argtypes = (POINTER(c_float), c_int)
libalex.sum.restype = c_float

def alex_sum(tab):
    ftab = [float(e) for e in tab]
    ftab = (c_float * len(ftab))(*ftab)
    return libalex.sum(ftab, len(ftab))


