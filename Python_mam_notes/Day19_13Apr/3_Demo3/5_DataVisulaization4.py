# -*- coding: utf-8 -*-
"""
@author: Jamgaonkar
"""

import matplotlib.pyplot as plt

y = [20, 30, 40]
x = [0, 1, 2]

# it will give all bars red color
plt.bar(x, y, width=[1.2, 2.0, 1.2], color='red')
plt.show()

# it will give red green blue respectively
plt.bar(x, y, width=[1.2, 1.0, 1.2], color=['red', 'green', 'blue'])
plt.legend(["Red", "Green", "Blue"], loc="lower right")
plt.show()

# alignment
plt.title('The posts in different blogs')
plt.xlabel('blogs', fontsize=15)
plt.ylabel('posts', fontsize=15)
# plt.show()

plt.bar(x, y, width=[0.5, 0.7, 1.0], color='red', align='edge')
plt.show()
