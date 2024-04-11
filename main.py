from load_data import load_data
from sort import bubble_sort
import matplotlib.pyplot as plt
import numpy as np

load_data('activity.csv')
data = load_data('activity.csv')
power_W = data['PowerOriginal']

sorted_power_W = bubble_sort(power_W)
print(sorted_power_W[::-1])

time = np.array(range(0, len(sorted_power_W)))
time = time/60
plt.plot(time, sorted_power_W[::-1])
plt.xlabel('Time')
plt.ylabel('Power')
plt.grid(True)

#save in figures
plt.savefig('figures/plot.png')
plt.show()



