import matplotlib
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,10,100)

# 1.
# plt.figure()
# plt.subplot(2,1,1)
# plt.plot(x,np.sin(x))
#
# plt.subplot(2,1,2)
# plt.plot(x,np.cos(x))
#
# plt.show()

# 2.
# fig,ax=plt.subplots(2)
# ax[0].plot(x,np.sin(x))
# ax[1]=plt.plot(x,np.cos(x))


# 3.
fig=plt.figure()
ax=plt.axes()
ax.plot(x,np.sin(x))

plt.show()

