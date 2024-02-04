import numpy as np
import matplotlib.pyplot as plt

# color = ['blue', 'blue', 'blue', 'blue', 'green', 'red']

# LOL_v1_method = ['DeepUPE', 'RetinexNet', 'RUAS', 'KinD', 'SNR-Net', 'Retinexformer']

# LOL_v1_value = [14.38, 16.77, 18.23, 20.86, 24.61, 25.16]

color = ['blue', 'blue', 'blue', 'blue', 'red']

SMID_method = ['KinD', 'DUPE', 'RUAS', 'ReNet', 'Ours']

SMID_value = [13.29, 15.08, 16.55, 17.13, 25.67]

plt.bar(SMID_method, SMID_value, width = 0.6, color = color, linewidth = 1)

# plt.yscale('log')
plt.ylim(13,26)

plt.xticks(fontsize=18)

plt.yticks(fontsize=18)

# plt.savefig('SMID.png')
plt.savefig('LOL_v2_syn.png')
plt.savefig('LOL_v2_syn.pdf')