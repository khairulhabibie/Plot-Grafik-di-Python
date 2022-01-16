## set axis

import matplotlib.pyplot as plt
import numpy as np

# membuat plot (sin(2wt + theta))
def sinusGenerator(amplitudo,frekuensi,tAhkhir,theta):
    t = np.arange(0,tAhkhir,0.1)
    y = amplitudo * np.sin(2*frekuensi*t + np.deg2rad(theta))
    return t,y

t,y = sinusGenerator(1,1,4,0)

# membuat plot
plt.plot(t,y)

# set axis : maximum dan minimum
# plt.axis([xmin, xmax, ymin, ymax])
plt.axis([0, 4, -1, 1])

# menampilkan
plt.show()