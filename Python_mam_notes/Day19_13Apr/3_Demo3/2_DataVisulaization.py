# -*- coding: utf-8 -*-
"""
@author: Jamgaonkar
"""

import matplotlib.pyplot as plt

subject = ['English Core', 'Mathematics', 'Physics', 'Chemistry', 'I.P.']
percentage = [83, 95, 70, 89, 100]

plt.bar(subject, percentage, align='center', color='blue')
plt.xlabel('Subject Name')
plt.ylabel('Percentage')
plt.legend(['Single Element'])
plt.title('Result Analysis Bar Graph  ')
plt.show()
