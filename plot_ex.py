"""
这是Python Matplotlib模板的一个示例: 曲线图
点击右键 ->【运行当前文件】查看效果

了解更多关于Matplotlib的使用方法, 点击这里查看官方文档: https://matplotlib.org/stable/users/index
"""
# -----------------------------------------------------------------------------
# Copyright (c) 2015, Nicolas P. Rougier. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

n = 256
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
Y = np.sin(2*X)

plt.axes([0.025, 0.025, 0.95, 0.95])

plt.plot(X, Y+1, color='blue', alpha=1.00)
plt.fill_between(X, 1, Y+1, color='blue', alpha=.25)

plt.plot(X, Y-1, color='blue', alpha=1.00)
plt.fill_between(X, -1, Y-1, (Y-1) > -1, color='blue', alpha=.25)
plt.fill_between(X, -1, Y-1, (Y-1) < -1, color='red',  alpha=.25)

plt.xlim(-np.pi, np.pi), plt.xticks([])
plt.ylim(-2.5, 2.5), plt.yticks([])

plt.show()
