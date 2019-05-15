# -*- coding: utf-8 -*-
"""
Created on Fri May  3 15:54:10 2019

@author: Victoria
"""
#We can use a power analysis to help determine how many samples needed to observe a certain effect with a statistical test
#We can use the statsmodels.stats power function solve_power to help us find the variable we are looking for
#In this case, we are looking for the number of samples needed
#Inputs are an effect size,nobs,significance level, and target power. 
#Effect size for this project is the significant difference between particle diameters 
#divided by the standard deviation of the means of the samples collected from the dunes, which are our control samples 
#nobs is the number of samples needed
#significance level is alpha = 0.05 for a significance level of 95%
#target power is 1-beta, usually 0.8
#None is used for the variable we are trying to find
#Output will be the variable you are trying to find, in this case nobs
from __future__ import print_function

from statsmodels.stats import power as p

samplenumber = p.FTestAnovaPower().solve_power(effect_size=2.6,nobs=None,alpha=0.05,power=0.8)
print(samplenumber)