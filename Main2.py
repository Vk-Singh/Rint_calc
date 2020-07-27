import numpy as np
import pandas as pd
import matplotlib
#import matplotlib.pyplot as plt
#from matplotlib import pyplot


import scipy
from scipy.optimize import curve_fit

def func(x, m, c):
    return m*x +c


my_dict = {}

f = open("data.txt", "r")

for x in f:

    if x == '\n':
        pass

    else:

        splitlist = x.split()

        if splitlist[0] in my_dict:
            my_dict[splitlist[0]].append(splitlist[1])
        else:
            my_dict[splitlist[0]] = [splitlist[1]]


print(my_dict)
f.close()
df=pd.DataFrame.from_dict(my_dict,orient='index').transpose()
print(df)
df = df.reindex(sorted(df.columns), axis=1)


df.to_csv("Output1.csv")

column_list = df.columns.values.tolist()
np_voltage = np.asarray(column_list, dtype=np.float32)

final_result=[]

for index, rows in df.iterrows():

    current_values_list =[]
    for x in column_list:
        current_values_list.append(float(rows[x]))

    np_current = np.asarray(current_values_list, dtype=np.float32)

    popt, pcov = scipy.optimize.curve_fit(func, np_voltage, np_current) # your data x, y to fit

    final_result.append(1/popt[0])
print(final_result)

#hist, bin_edges = np.histogram(final_result)
#print (hist)
#print (bin_edges)
#
"""
n, bins, patches = matplotlib.pyplot.hist(x=final_result, bins='auto', color='#0504aa',
                            alpha=0.7, rwidth=0.85)
matplotlib.pyplot.grid(axis='y', alpha=0.75)
matplotlib.pyplot.xlabel('Value')
matplotlib.pyplot.ylabel('Frequency')
matplotlib.pyplot.title('My Very Own Histogram')
matplotlib.pyplot.text(23, 45, r'$\mu=15, b=3$')
maxfreq = n.max()
# Set a clean upper y-axis limit.
matplotlib.pyplot.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
"""
df_final = pd.DataFrame(final_result , columns =['Resistance'])
df_final.to_csv("FinalResults.csv")