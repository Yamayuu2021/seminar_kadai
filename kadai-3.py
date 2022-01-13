import matplotlib.pyplot as plt
import numpy as np

Year = [2014,2015,2016,2017,2018,2019]
Opencampus = [1452,1796,1894,2584,2735,3447]
Aspirants = [3231,3747,3726,5853,8866,10913]

plt.scatter(Aspirants,Opencampus, label='Aspirant', color='aqua')

plt.xlabel("Aspirants")
plt.ylabel("OpenCampus")

plt.legend()
plt.show()