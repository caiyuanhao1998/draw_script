import numpy as np
import matplotlib.pyplot as plt

# color = ['blue', 'blue', 'blue', 'blue', 'green', 'red']

# LOL_v1_method = ['DeepUPE', 'RetinexNet', 'RUAS', 'KinD', 'SNR-Net', 'Retinexformer']

# LOL_v1_value = [14.38, 16.77, 18.23, 20.86, 24.61, 25.16]

color = ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'orange', 'red']

bisci_method = ['BiConnect', 'BNN', 'Bi-Real', 'IRNet', 'ReActNet', 'BBCU', 'BTM', 'λ-Net' ,'BiSRNet']

bisci_value = [22.19, 23.88, 26.26, 26.30, 26.48, 26.51, 27.21, 28.53, 29.76]

plt.figure(num=3,figsize=(22,5))

plt.bar(bisci_method, bisci_value, width = 0.4, color = color, linewidth = 1)

# plt.yscale('log')
plt.ylim(21,30.3)

plt.xticks(fontsize=18)

plt.yticks(fontsize=18)



plt.savefig('BiSCI_teaser_v2.png')

plt.savefig('BiSCI_teaser_v2.pdf')