import pandas as pd
import numpy as np

dive = pd.read_csv("C:\Users\lsong\Documents\GitHub", index_col = None,  header = 0,  low_memory = False,  na_values = '?')
seahorse = pd.read_csv("C:\Users\lsong\Documents\GitHub", index_col = None,  header = 0,  low_memory = False,  na_values = '?')

environment = ['PENCIL_URCHIN', 'HYDROZOAN', 'SOFT_CORAL', 'ANEMONE', 'SPONGE_SOL', 'SPONGE_SUB', 'SEAPEN', 'SEAGRASS', 'SHELL']

melt = pd.melt(dive, id_vars = ['DATE',  'SITE', 'LONGITUDE',  'LATITUDE', 'DEPTH', 'SST', 'BT', 'VISIBILITY', 'SEAHORSES'], value_vars = environment)

melt.to_csv(r'C:\Users\lsong\Desktop\melt_dive_sh.csv')
