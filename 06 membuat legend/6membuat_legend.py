## membuat legend

import matplotlib.pyplot as plt
import numpy as np

#membuat plot (sin(2wt + theta))
def sinusGenerator(amplitudo,frekuensi,tAhkhir,theta):
    t = np.arange(0,tAhkhir,0.1)
    y = amplitudo * np.sin(2*frekuensi*t + np.deg2rad(theta))
    return t,y

t1,y1 = sinusGenerator(1,1,4,0)
t2,y2 = sinusGenerator(1,1,4,90)

# membuat plot
#tipe 1
#plt.plot(t1,y1, label="sin(0)")
#plt.plot(t2,y2, label="sin(90)")
#plt.legend()

#tipe 2
#plt.plot(t1,y1, label="sin(0)")
#plt.plot(t2,y2, label="sin(90)")
#plt.legend(loc="upper center")

#tipe 3
#plt.plot(t1,y1, label="sin(0)")
#plt.plot(t2,y2, label="sin(90)")
#plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.5))

#tipe 4
plt.figure(1)
ax = plt.subplot(111)
plt.plot(t1,y1, label="sin(0)")
plt.plot(t2,y2, label="sin(90)")
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width*0.8, box.height])
plt.legend(loc="upper center", bbox_to_anchor=(1.2,1))

# menampilkan
plt.show()