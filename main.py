from load_data import load_data
from sort import bubble_sort
import matplotlib.pyplot as plt

load_data('activity.csv')
data = load_data('activity.csv')
power_W = data['PowerOriginal']

sorted_power_W = bubble_sort(power_W)
print(sorted_power_W[::-1])

plt.plot(sorted_power_W[::-1])


#save in figures
plt.savefig('figures/plot.png')
plt.show()



