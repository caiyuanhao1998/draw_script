# This is a sample Python script.
import matplotlib.pyplot as plt
import math
import numpy as np
# Example data
models = ['TensoRF', 'InTomo', 'NeRF', 'NeAT', 'NAF','X-Gaussians']
fps  = [0.77, 0.62, 0.14, 1.78, 2.01, 148]  # FLOPS (G) in logarithmic scale
psnr = [30.447, 30.187, 30.289, 34.021, 36.942, 43.404]  # PSNR (dB)
params = [178 , 125, 313, 69, 63, 9]  # Model parameters in millions
bubble_sizes = [size * 45 for size in params]  # Scale the bubble sizes
bubble_sizes[0] = bubble_sizes[0]*0.6
bubble_sizes[1] = bubble_sizes[1]*0.6
bubble_sizes[2] = bubble_sizes[2]*0.82
bubble_sizes[3] = bubble_sizes[3]*0.4
bubble_sizes[4] = bubble_sizes[4]*0.4
bubble_sizes[5] = bubble_sizes[5]*0.3
# bubble_sizes[5] = bubble_sizes[5]*1
color = ['cornflowerblue', 'moccasin', 'y', 'teal' , 'orange', 'r']
alphas = [0.3, 1., 0.4, 0.4, 0.5, 0.5]
# Create scatter plot
# fig, ax = plt.subplots()
# Initialize figure
#fig = plt.figure(num=None, figsize=(12, 12), facecolor='w', edgecolor='k')
# fig.patch.set_facecolor('white')
# fig.patch.set_alpha(1)
# ax = plt.gca()

fig, ax = plt.subplots(figsize=(12, 12))
scatter = ax.scatter(fps, psnr, s=bubble_sizes, alpha=alphas, c = color, edgecolor="none")



# Logarithmic scale for the x-axis
ax.set_yticks([25,30,35,40,45])
ax.set_xscale('log')
ax.set_xticks([1e-2,1e-1,1,1e1,1e2])
plt.tick_params(axis="both", which="major", direction="in", width=3, length=5, pad=5)
plt.yticks(fontsize=25)
plt.xticks(fontsize=25)

ax.set_xticklabels([])
ax.set_yticklabels([])

bwith = 2 #边框宽度设置为2
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
# Labels and title
# ax.set_xlabel('FPS (log)',fontsize=25)
# ax.set_ylabel('PSNR (dB)',fontsize=25)

# Grid
ax.grid(True, which='both', linestyle='--', linewidth=0.5,alpha = 0.2)

plt.savefig('plot.pdf')
# Show the plot
# plt.show()