import matplotlib.pyplot as plt
import time 

from modules.game_of_lifePYTHON import update as up0
from modules.game_of_lifePYTHON import update_rule as upr0

from modules.cython_1_0 import update as up1
from modules.cython_1_0 import update_rule as upr1

from modules.cython_2_0 import update as up2
from modules.cython_2_0 import update_rule as upr2

from modules.cython_3_0 import update as up3
from modules.cython_3_0 import test_update_rule as upr3

from modules.cython_4_0 import update as up4
from modules.cython_4_0 import test_update_rule as upr4



lattice = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]
]

def benchmark_update(update_func, lattice, iterations=1000):
    start_time = time.time()
    for _ in range(iterations):
        update_func(lattice)
    end_time = time.time()
    return (end_time - start_time) / iterations


times = {
    'Python': benchmark_update(up0, lattice),
    'Cython 1': benchmark_update(up1, lattice),
    'Cython 2': benchmark_update(up2, lattice),
    'Cython 3': benchmark_update(up3, lattice),
    'Cython 4': benchmark_update(up4, lattice),
}

# Plot the results
labels, time_values = zip(*times.items())
plt.bar(labels, time_values, color='blue')
plt.ylabel('Time (sec)')
plt.title('Results')
plt.annotate('Over a 6x speed up\nLarger speed-ups are possible, for the\nMandelbrot set (exercise 4) the speed\nup is ~250x', 
             xy=(2.5, max(time_values)), xytext=(3, max(time_values)+1),
             arrowprops=dict(facecolor='black', shrink=0.05),
             )
plt.show()

