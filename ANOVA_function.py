# -*- coding: utf-8 -*-
"""
Created on Thu May  2 18:33:42 2019

@author: Victoria
"""
import numpy as np
from scipy import stats
import pandas as pd

mean_data = pd.read_csv('file:///C:/Users/Victoria/Documents/Data Analytics/Final Project/analysis/Mean_Data.csv')
print (mean_data)

fi = np.isfinite(mean_data['Log'])
mean_data['Log'][fi]
F,p = stats.f_oneway(mean_data['Log'][fi], mean_data['Hay'], mean_data['NP'], mean_data['Dune'])
print (F,p)

if p < .05:
    print('We reject the null hypothesis')
else: 
    print('We fail to reject the null hypothesis and do not have to complete a Post-Hoc Test')


mean_array =[]
for values in mean_data:
    mean_array = np.append([mean_array],[values],axis=None)
    print(values)
print(mean_array)


empty_array=[]
variable_array =[1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]      #fix so that the number corresponds to how many columns
for values in variable_array:
    empty_array = np.append([empty_array],[mean_array], axis=None)
    print(values)
print(variable_array)


from statsmodels.stats.multicomp import MultiComparison
mc = MultiComparison(mean_array, variable_array)
result = mc.tukeyhsd()
print(result)
#this is a comparison of all of the possible means and their differences. 
#This also shows us the upper and lower limits of the means according to a 95% confidence interval. 
#It also shows us if we should reject or fail to reject the null hypothesis with a 95 % confidence.
#Our null hypothesis is that there is no significant difference between temperature samples obtained 
#from three different CTDs sitting in the same calibration bath
#The multicomparison helps us see the significant differences in our means.