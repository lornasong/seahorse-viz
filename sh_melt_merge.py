import pandas as pd
import numpy as np

#Assumes dive and seahorse CSVs share SITE and DATE columns to join on.

dive = pd.read_csv("C:\Users\lsong\Documents\GitHub\sh-data-format\dive_data.csv", index_col = None,  header = 0,  low_memory = False,  na_values = '')
seahorse = pd.read_csv("C:\Users\lsong\Documents\GitHub\sh-data-format\seahorse_data.csv", index_col = None,  header = 0,  low_memory = False,  na_values = '')

environment = ['PENCIL_URCHIN', 'HYDROZOAN', 'SOFT_CORAL', 'ANEMONE', 'SPONGE_SOL', 'SPONGE_SUB', 'SEAPEN', 'SEAGRASS', 'SHELL']

merge = pd.merge(dive,  seahorse,  how = "left",  on = ["SITE",  "DATE"])

#merge.to_csv(r'C:\Users\lsong\Desktop\merge.csv')

melt = pd.melt(merge, id_vars = ['DATE',  'SITE', 'LONGITUDE',  'LATITUDE', 'DEPTH', 'SST', 'BT', 'VISIBILITY', 'SEAHORSES'], value_vars = environment)

#melt.to_csv(r'C:\Users\lsong\Desktop\melt_dive_sh.csv')
