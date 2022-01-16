import numpy as np
import matplotlib.pyplot as plt

"""
    1. Membuat data
    2. membuat plot
    3. menampilkan plot
"""

# 1. membuat data
x = np.array([1,2,3,4,5])
y = np.array([1,2,3,4,5])
y2 = np.array([1,4,9,16,25])

# 2. membuat plot
plt.plot(x,y)
plt.plot(x,y2)

# 3. menampilkan plot
plt.show()
