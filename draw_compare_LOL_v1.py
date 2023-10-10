import numpy as np
import matplotlib.pyplot as plt

# color = ['blue', 'blue', 'blue', 'blue', 'green', 'red']

# LOL_v1_method = ['DeepUPE', 'RetinexNet', 'RUAS', 'KinD', 'SNR-Net', 'Retinexformer']

# LOL_v1_value = [14.38, 16.77, 18.23, 20.86, 24.61, 25.16]

color = ['blue', 'blue', 'blue', 'blue', 'red']

LOL_v1_method = ['DUPE', 'ReNet', 'RUAS', 'KinD', 'Ours']

LOL_v1_value = [14.38, 16.77, 18.23, 20.86, 25.16]

plt.bar(LOL_v1_method, LOL_v1_value, width = 0.6, color = color, linewidth = 1)

# plt.yscale('log')
plt.ylim(14,26)

plt.xticks(fontsize=18)

plt.yticks(fontsize=18)

plt.savefig('LOL_v1_no_snr.png')

plt.savefig('LOL_v1_no_snr.pdf')