import numpy as np
from sklearn.manifold import TSNE
import os
import numpy as np
# import numpy as np
import matplotlib.pyplot as plt

#
# 7571 cntzero
# 0 cntaf
# 76851 cntfm
def eq(a, b):
    return abs(a - b) < 0.001

def is_ferromagnetic(arr):
    if (eq(arr[0], 0)):
        return False
    if (all(eq(a, arr[0]) for a in arr)):
        return True
    return False

def is_zero(arr):
    if (all([eq(a, 0) for a in arr])):
        return True
    return False

def is_antiferromagnetic(arr):
    x1 = arr[0]
    x2 = arr[1]
    if (eq(x1, 0) or not (eq(x1, x2))):
        return False
    for i in range(0, 8):
        for j in range(0, 8):
            cur = i * 8 + j
            if ((i + j)% 2) == 0:
                if (not eq(arr[cur], x1)):
                    return False
            else:
                if (not eq(arr[cur], x2)):
                    return False
    return True

# is_antiferromagnetic([])
dirData = 'large_nf_InvertZY2'
nset = 'large_set1'
wData = np.genfromtxt(os.path.join('.', dirData, (nset + '_W' + '.dat')))
cntwj = wData.size
jData = np.genfromtxt(os.path.join('.', dirData, (nset + '_J' + '.dat')))
snz10 = np.genfromtxt(os.path.join('.', dirData, (nset + '_Z' + '.dat')))
snx10 = np.genfromtxt(os.path.join('.', dirData, (nset + '_X' + '.dat')))
sny10 = np.genfromtxt(os.path.join('.', dirData, (nset + '_Y' + '.dat')))

labels = []

cntzero = 0
cntaf = 0
cntfm  = 0
for z in snz10:
    # print(z)
    if (is_zero(z)):
        labels.append(0)
        cntzero+=1
    elif (is_ferromagnetic(z)):
        labels.append(1)
        cntfm+=1
    elif (is_antiferromagnetic(z)):
        labels.append(2)
        cntaf+=1
    else:
        labels.append(3)
    print(labels[-1])


np.savetxt(os.path.join('.', dirData, nset + '__labels.dat'), np.array(labels, dtype=int).astype(int))

print("RESULTS")
print(cntzero, "cntzero")
print(cntaf, "cntaf")
print(cntfm, "cntfm")
# np.array(labels)
# np.savetxt(os.path.join('.', dirData, (nset + '_labels' + '.dat')), labels)
