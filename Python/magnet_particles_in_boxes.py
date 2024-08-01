import numpy as np
from numpy import inf
def doubles(maxk, maxn):
    total_f = 0
    for k in range(1, maxk+1):
        total = (1/(k*np.arange(2, maxn+2)**(2*k)))
        total[total == inf] = 0
        total_f += np.sum(total)
    return total_f