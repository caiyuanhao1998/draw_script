import numpy as np
import matplotlib.pyplot as plt

# color = ['blue', 'blue', 'blue', 'blue', 'green', 'red']

# LOL_v1_method = ['DeepUPE', 'RetinexNet', 'RUAS', 'KinD', 'SNR-Net', 'Retinexformer']

# LOL_v1_value = [14.38, 16.77, 18.23, 20.86, 24.61, 25.16]

color = ['blue', 'blue', 'blue', 'blue', 'red']

SID_method = ['ReNet', 'DUPE', 'KinD', 'RUAS',  'Ours']

SID_value = [16.48, 17.01, 18.02, 18.44, 24.44]

plt.bar(SID_method, SID_value, width = 0.6, color = color, linewidth = 1)

# plt.yscale('log')
plt.ylim(16,25)

plt.xticks(fontsize=18)

plt.yticks(fontsize=18)

plt.savefig('SID.png')
plt.savefig('SID.pdf')