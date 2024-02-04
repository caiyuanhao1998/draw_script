"""
这是Python Matplotlib模板的一个示例: 量场图
点击右键 ->【运行当前文件】查看效果

了解更多关于Matplotlib的使用方法, 点击这里查看官方文档: https://matplotlib.org/stable/users/index
"""
# -----------------------------------------------------------------------------
# Copyright (c) 2015, Nicolas P. Rougier. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

n = 8
X, Y = np.mgrid[0:n, 0:n]
T = np.arctan2(Y-n/2.0, X-n/2.0)
R = 10+np.sqrt((Y-n/2.0)**2+(X-n/2.0)**2)
U, V = R*np.cos(T), R*np.sin(T)

plt.axes([0.025, 0.025, 0.95, 0.95])
plt.quiver(X, Y, U, V, R, alpha=.5)
plt.quiver(X, Y, U, V, edgecolor='k', facecolor='None', linewidth=.5)

plt.xlim(-1, n), plt.xticks([])
plt.ylim(-1, n), plt.yticks([])

plt.show()
