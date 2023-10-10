import numpy as np
import matplotlib.pyplot as plt

# color = ['blue', 'blue', 'blue', 'blue', 'green', 'red']

# LOL_v1_method = ['DeepUPE', 'RetinexNet', 'RUAS', 'KinD', 'SNR-Net', 'Retinexformer']

# LOL_v1_value = [14.38, 16.77, 18.23, 20.86, 24.61, 25.16]

# color = ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'red']

# color = ['orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'blue']

# color = ['royalblue', 'royalblue', 'royalblue', 'royalblue', 'royalblue', 'royalblue', 'royalblue', 'lightcoral']

category = ['medicine', 'biology', 'security', 'industry']

color = ['cornflowerblue', 'cornflowerblue', 'cornflowerblue', 'cornflowerblue', 'cornflowerblue', 'lightcoral']

method = ['Intratomo', 'NeRF', 'NeAT', 'TensoRF', 'NAF', 'SAX-NeRF']

medicine_proj_psnr = [31.10, 33.10, 36.06, 35.27, 39.87, 50.78]

biology_proj_psnr = [31.65, 29.15, 39.14, 42.58, 39.31, 57.61]

security_proj_psnr = [35.37, 27.88, 38.87, 39.30, 39.00, 43.43]

industry_proj_psnr = [32.75, 37.71, 29.83, 41.95, 33.30, 55.71]

plt.figure(num=3,figsize=(20,5))

plt.bar(bisci_method, bisci_value, width = 0.4, color = color, linewidth = 1)

# plt.yscale('log')
plt.ylim(21,30.3)

plt.xticks(fontsize=18)

plt.yticks(fontsize=18)



plt.savefig('BiSCI_teaser.png')

plt.savefig('BiSCI_teaser.pdf')