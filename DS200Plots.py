#!/usr/bin/env python
# coding: utf-8

# In[167]:


import numpy as np
import pandas as pd
from pandas import DataFrame, read_csv

import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm


# In[168]:


plt.rc('font', size=16)          # controls default text sizes
plt.rc('axes', titlesize=18)     # fontsize of the axes title
plt.rc('axes', labelsize=16)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=16)    # fontsize of the tick labels
plt.rc('ytick', labelsize=16)    # fontsize of the tick labels
plt.rc('legend', fontsize=12.5)    # legend fontsize
plt.rc('figure', titlesize=14)  # fontsize of the figure title


# In[169]:


file1 = r'data/faculties.xls'


# In[170]:


file2 = r'data/lpg.xls'


# In[171]:


data = pd.read_excel(file1)


# In[172]:


data2 = pd.read_excel(file2)


# In[173]:


data


# In[174]:


data2


# In[175]:


insti = data["Name of Institute"]


# In[176]:


facultyP = data["Faculty in Position"]


# In[177]:


facultyS = data["Sanctioned Strength"]


# In[178]:


sector = data2["Sector"]


# In[179]:


x2012=data2["2012-13"]
x2013=data2["2013-14"]
x2014=data2["2014-15"]
x2015=data2["2015-16"]
x2016=data2["2016-17"]
x2017=data2["2017-18"]
x2018=data2["2018-19 (P)"]


# In[180]:


combined = np.vstack((x2012, x2013, x2014, x2015, x2016, x2017, x2018)).T


# In[181]:


fig, barplot = plt.subplots(figsize = (15,9))
y1 = facultyP[0:23]
width = 0.5
barplot.bar(np.arange(len(y1)), y1, width=width, color='green')  
x=np.arange(23)
plt.title("Faculties in position in IITs")
barplot.set_xticks(x)
barplot.set_xticklabels(insti[0:23], rotation = 90)
barplot.set_ylabel('No. of faculties')
barplot.set_xlabel('Institute')   
plt.savefig('plots/faculties_bar.png',dpi=300,bbox_inches='tight')
fig.tight_layout()


# In[182]:


plt.figure(2, figsize = (9,7))
plt.scatter(facultyS[0:23],facultyP[0:23],color='blue')
plt.title("Strength vs in position")
plt.ylabel('Faculties in position')
plt.xlabel('Sanctioned strength')
plt.savefig('plots/faculties_scatter.png',dpi=300,bbox_inches='tight')
fig.tight_layout()


# In[183]:


plt.figure(3, figsize = (9,7))
plt.boxplot(combined)
plt.xticks([1, 2, 3, 4, 5, 6, 7], ['2012-13', '2013-14','2014-15', '2015-16', '2016-17', '2017-18','2018-19'],
           rotation = 65)
plt.yscale("log")
plt.title("Strength vs in position")
plt.ylabel('LPG Distriubution')
plt.xlabel('Year') 
plt.savefig('plots/lpg_box.png',dpi=300,bbox_inches='tight')
plt.show()


# In[ ]:




