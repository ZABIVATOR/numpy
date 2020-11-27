import numpy
import matplotlib.pyplot as plt
with open ('signals/signal01.dat') as f:
	sign = list(map(float, f.read().split()))
a = numpy.array([sign]).transpose()
b=[]
for i in range (10):
	b.append(numpy.mean(a[0:i+1]))
for i in range (10,a.size):
	b.append(numpy.mean(a[i-10:i]))
fig, ax = plt.subplots(1,2)
ax[0].plot(range(100), a)
ax[1].plot(range(100), b)
ax[0].set_title('Raw signal')
ax[1].set_title('Filtered signal')
plt.show()
