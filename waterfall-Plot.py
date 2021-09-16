#!/usr/bin/python

# LOCAL PATH: C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64>

import matplotlib.pyplot as plt
from blimpy import Waterfall

file_path = 'C:\\Users\\arunm\\Downloads\\Voyager1.single_coarse.fine_res.h5'
obs = Waterfall(file_path)
obs.plot_waterfall(f_start=8419.2740, f_stop=8419.2750)
plt.savefig('C:\\Users\\arunm\\Downloads\\waterfall.png', bbox_inches='tight')
