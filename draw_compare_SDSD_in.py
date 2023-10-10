import numpy as np
import matplotlib.pyplot as plt

# color = ['blue', 'blue', 'blue', 'blue', 'green', 'red']

# LOL_v1_method = ['DeepUPE', 'RetinexNet', 'RUAS', 'KinD', 'SNR-Net', 'Retinexformer']

# LOL_v1_value = [14.38, 16.77, 18.23, 20.86, 24.61, 25.16]

color = ['blue', 'blue', 'blue', 'blue', 'red']

SDSD_method = ['ReNet', 'DUPE', 'KinD', 'RUAS',  'Ours']

SDSD_value = [20.84, 21.70, 21.95, 23.17, 29.77]

plt.bar(SDSD_method, SDSD_value, width = 0.4, color = color, linewidth = 1)

# plt.yscale('log')
plt.ylim(20,30)

plt.xticks(fontsize=18)

plt.yticks(fontsize=18)

plt.savefig('SDSD_in.png')
plt.savefig('SDSD_in.pdf')