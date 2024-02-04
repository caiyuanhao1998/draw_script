"""
这是Python Matplotlib模板的一个示例:条形图
点击右键 ->【运行当前文件】查看效果

了解更多关于Matplotlib的使用方法, 点击这里查看官方文档: https://matplotlib.org/stable/users/index
"""
# -----------------------------------------------------------------------------
# Copyright (c) 2015, Nicolas P. Rougier. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

n = 12
X = np.arange(n)
Y1 = (1-X/float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1-X/float(n)) * np.random.uniform(0.5, 1.0, n)

plt.axes([0.025, 0.025, 0.95, 0.95])
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

for x, y in zip(X, Y1):
    plt.text(x+0.4, y+0.05, '%.2f' % y, ha='center', va='bottom')

for x, y in zip(X, Y2):
    plt.text(x+0.4, -y-0.05, '%.2f' % y, ha='center', va='top')

plt.xlim(-.5, n), plt.xticks([])
plt.ylim(-1.25, +1.25), plt.yticks([])

plt.savefig('bar_ex.png')
