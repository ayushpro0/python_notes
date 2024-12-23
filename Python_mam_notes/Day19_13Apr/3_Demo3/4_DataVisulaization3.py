# -*- coding: utf-8 -*-
"""
@author:Jamgaonkar
"""

import matplotlib.pyplot as plt

x = [0, 1, 2]
y = [10, 15, 5]
plt.bar(x, y)
plt.show()

plt.bar(x, y, width=1.1)
plt.show()

plt.bar(x, y, width=0.5)
plt.show()

plt.bar(x, y, width=0.2)
plt.show()

plt.bar(x, y, width=[1.1, 0.8, 0.2])
plt.show()

plt.bar(x, y, width=[1, 0.8, 1.3], color='r')
plt.show()
