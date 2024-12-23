# -*- coding: utf-8 -*-
"""

@author:Jamgaonkar
"""

import matplotlib.pyplot as plt

x = [5, 10, 15, 20, 25, 12]
y = [12, 5, 18, 20, 22]
plt.plot(x, marker='*', markersize=10)
plt.plot(y, marker='+', markeredgecolor='g', markersize=15)
plt.show()
