"""
这是Python Matplotlib模板的一个示例: 等高线图
点击右键 ->【运行当前文件】查看效果

了解更多关于Matplotlib的使用方法, 点击这里查看官方文档: https://matplotlib.org/stable/users/index
"""
# -----------------------------------------------------------------------------
# Copyright (c) 2015, Nicolas P. Rougier. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)


n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)

plt.axes([0.025, 0.025, 0.95, 0.95])

plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap=plt.cm.hot)
C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5)
plt.clabel(C, inline=1, fontsize=10)

plt.xticks([]), plt.yticks([])

plt.show()
