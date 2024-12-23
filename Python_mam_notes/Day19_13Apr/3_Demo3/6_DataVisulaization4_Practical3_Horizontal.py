# -*- coding: utf-8 -*-
"""
@author:Jamgaonkar
"""

# here we require both values X & Y & both Should be same size
import matplotlib.pyplot as plt

y = [20, 30, 40]
x = [0, 1, 2]

# it will give all bars red color
plt.bar(x, y, width=[1.2, 2.0, 1.2], color='red')
plt.show()

plt.bar(x, y, width=[1.2, 2.0, 1.2], color=['red', 'green', 'blue'])
plt.show()

# alignment
plt.title('The posts in different blogs')
plt.xlabel('blogs', fontsize=15)
plt.ylabel('posts', fontsize=15)
# plt.show()

plt.barh(x, y, height=[1.2, 2.0, 1.2], color='red', align='edge')
plt.show()
