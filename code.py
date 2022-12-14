# -*- coding: utf-8 -*-
"""Does maternal mortality fall as countries get richer?

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Timkp9SBqI4DY7iIh0xplZXant4GsXi4

In the article above, the author discussed the following question: **"Does maternal mortality fall as countries get richer?"**.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
import seaborn as sns
sns.set_theme(style="ticks")
from scipy import stats
from google.colab import files
import io

uploaded = files.upload()
data1 = pd.read_csv(io.BytesIO(uploaded['mmr_gdp_per_capita.csv']))
data1 = data1.astype({'gdp_per_capita' : 'float'})


uploaded = files.upload()
data2 = pd.read_csv(io.BytesIO(uploaded['GNI_per_capita.csv']))
data2 = data2.astype({'gni_per_capita' : 'float'})

uploaded = files.upload()
data3 = pd.read_csv(io.BytesIO(uploaded['data3_gni.csv']))
data3.columns = ['country', 'gni_1990', 'gni_2015']

print(data1)

print(data3.columns)

data3 = data3.reset_index(drop = True)
data3 = data3.replace({'null' : -1})
data3 = data3.astype({'gni_1990' : 'float'})
data3 = data3.astype({'gni_2015' : 'float'})
data3 = data3[data3['gni_1990'] >= 0]
data3 = data3[data3['gni_2015'] >= 0]
data3 = data3.reset_index(drop = True)

print(data3)

#each entity (country) can be classified in one of the 4 groups below
#we used the World Bank's thresholds for classifying countries into income groups
#low_income regroups low income and lower-middle income countries. Only for the purpose of our study
#hence middle_income represents upper-middle income countries
#transitioned denotes any countries that moved up the classifications (i.e. lower to middle or high income, middle to high income)

low_income = []
high_income = []
middle_income = []
transitioned = []

for i in range(len(data3)):
  if data3['gni_1990'][i] < 610:
    if data3['gni_2015'][i] < 1025:
      low_income.append(data3['country'][i])
    else:
      transitioned.append(data3['country'][i])
  elif data3['gni_1990'][i] >= 7620:
    if data3['gni_2015'][i] >= 12475:
      high_income.append(data3['country'][i])
    elif data3['gni_2015'][i] < 1025:
      low_income.append(data3['country'][i])
    else:
      middle_income.append(data3['country'][i])
  else: 
    if data3['gni_2015'][i] < 1025:
      low_income.append(data3['country'][i])
    elif data3['gni_2015'][i] >= 12475:
      transitioned.append(data3['country'][i])
    else:
      middle_income.append(data3['country'][i])
    
        
#verifications
print(len(low_income) + len(high_income) + len(transitioned) + len(middle_income), len(data3), "\nHigh Income: ", len(high_income), "\nLow Income: ", len(low_income), "\nMiddle Income: ", len(middle_income), "\nTransitioned: ", len(transitioned))

#Owing to pre-examination of the data, we observed a frequent error: some years we reported in negative values 
#such as year -1000
#we need to remove such errors
#in addition for our study, we would like to work with data from as early as 1980
#so we remove data from years before 1980
#we retain data from 1880 to the lastest possible year available in the data
#we also drop any row with no data at any variable. We need data on all variables
#it was hard to do, so we used na alternative. "trust the process"
data1 = data1.astype({'year' : 'int64'})
data1 = data1.replace('', 0)

data1 = data1[data1['year'] >= 1990]
data1 = data1.astype({'maternal_mortality_ratio' : 'float', 'gdp_per_capita' : 'float'})
data1 = data1[data1['gdp_per_capita'] > 0]
data1 = data1[data1['maternal_mortality_ratio'] > 0]

data1.to_excel("data1.xlsx")
print(data1)

#here again we want to work with the earliest and latest years available only
#we drop data from any other year
#and rename the columns for our convenience 
#merge the data after
#drop any entity for which we have data on one year only
#other it will distrub our calculations of the ratios

entities = np.unique(data1['entity'])

data1_min = data1[data1['year'] == 1990]
data1_max = data1[data1['year'] == 2015]

data1_min = data1_min.rename(columns = {'year' : 'first_year'})
data1_min = data1_min.rename(columns = {'maternal_mortality_ratio' : 'mmr_initial'})
data1_min = data1_min.rename(columns = {'gdp_per_capita' : 'gdp_per_capita_initial'})
data1_max = data1_max.rename(columns = {'year' : 'final_year'})
data1_max = data1_max.rename(columns = {'maternal_mortality_ratio' : 'mmr_final'})
data1_max = data1_max.rename(columns = {'gdp_per_capita' : 'gdp_per_capita_final'})

main_data = data1_min.merge(data1_max, how = 'left', on = 'entity')
main_data = main_data[main_data['first_year'] == 1990]
main_data = main_data[main_data['final_year'] == 2015]

print(min(main_data['first_year']))

#calcul of the rates of change
#and create these columns 

main_data['mmr_rate_of_change'] =  np.log(main_data['mmr_final'] / main_data['mmr_initial'])/(main_data['final_year'] - main_data['first_year'])
main_data['gdp_per_capita_rate_of_change'] = np.log(main_data['gdp_per_capita_final'] / main_data['gdp_per_capita_initial'])/(main_data['final_year'] - main_data['first_year'])

#assign each entity in our data to its appropriate income_group
#NA if that entity was not classified

group = []

for entity in main_data['entity']:
  if entity in low_income:
    group.append('Low Income')
  elif entity in high_income:
    group.append('High Income')
  elif entity in middle_income:
    group.append('Middle Income')
  elif entity in transitioned:
    group.append('Transitioned')
  else:
    group.append('NaN')

main_data['group'] = group
main_data = main_data[main_data['group'] != 'NaN']
print(len(group), np.unique(group, return_counts= True))
main_data = main_data[['entity', 'group', 'first_year', 'final_year', 'mmr_initial', 'mmr_final', 'gdp_per_capita_initial', 'gdp_per_capita_final', 'mmr_rate_of_change', 'gdp_per_capita_rate_of_change']]
main_data.to_excel("Final Output.xlsx")
print(main_data)

#graphs
graph = sns.jointplot(data = main_data, x="gdp_per_capita_rate_of_change", y="mmr_rate_of_change", hue="group", height = 6)
graph.set_axis_labels("Average annual change of GDP per capita", "Average annual change of maternal mortality ratio")

# Form a facetgrid using columns with a hue
g = sns.FacetGrid(main_data, hue="group", col = "group", height = 4)
g.map(sns.regplot, "gdp_per_capita_rate_of_change", "mmr_rate_of_change", ci = None)
g.set_axis_labels("Average annual change in GDP per capita", "Average annual change in maternal mortality ratio")

data_low = main_data[main_data['group'] == 'Low Income']
data_middle = main_data[main_data['group'] == 'Middle Income']
data_trans = main_data[main_data['group'] == 'Transitioned']
data_high = main_data[main_data['group'] == 'High Income']

p_low = stats.linregress(data_low["gdp_per_capita_rate_of_change"], data_low["mmr_rate_of_change"]).pvalue
p_middle = stats.linregress(data_middle["gdp_per_capita_rate_of_change"], data_middle["mmr_rate_of_change"]).pvalue
p_trans = stats.linregress(data_trans["gdp_per_capita_rate_of_change"], data_trans["mmr_rate_of_change"]).pvalue
p_high = stats.linregress(data_high["gdp_per_capita_rate_of_change"], data_high["mmr_rate_of_change"]).pvalue

slope_low = stats.linregress(data_low["gdp_per_capita_rate_of_change"], data_low["mmr_rate_of_change"]).slope
slope_middle = stats.linregress(data_middle["gdp_per_capita_rate_of_change"], data_middle["mmr_rate_of_change"]).slope
slope_trans = stats.linregress(data_trans["gdp_per_capita_rate_of_change"], data_trans["mmr_rate_of_change"]).slope
slope_high = stats.linregress(data_high["gdp_per_capita_rate_of_change"], data_high["mmr_rate_of_change"]).slope

p_values = [p_low, p_middle, p_trans, p_high]
slopes = [slope_low, slope_middle, slope_trans, slope_high]
Summary = pd.DataFrame(data = [p_values, slopes], index = ['p-value', 'slope'], columns = ['Low Income', 'Middle Income', 'Transitioned', 'High Income']) 
print(Summary)

"""#Link to the OWiD author's visualization: [HERE](https://ourworldindata.org/grapher/maternal-mortality-ratio-vs-gdp-per-capita)"""
