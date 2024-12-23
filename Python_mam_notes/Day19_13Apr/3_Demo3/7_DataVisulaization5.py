# -*- coding: utf-8 -*-
"""
@author:Jamgaonkar
"""

import matplotlib.pyplot as plt

x = [5, 10, 15, 20, 25]
y = [12, 4, 15, 18, 12]
plt.plot(x, y)
plt.show()

plt.plot(x, y, color='r')
plt.show()

plt.plot(x, y, color='r', marker='*')
plt.show()

plt.plot(x, y, color='r', marker='*', markeredgecolor='b')
plt.show()

plt.plot(x, y, color='r', marker='*', markeredgecolor='b', linewidth=10)
plt.show()

plt.plot(x, y, color='r', marker='*', markeredgecolor='b', linewidth=10, linestyle="dotted")
plt.show()
