#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 09:55:51 2023

@author: jen
"""

#LOAD THE PACKAGES

import os
import matplotlib as mpl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


os.chdir("/Users/jen/jen/dssg/datathon_mar_23")

# import original unaltered data
orgdf = pd.read_csv('main_export.csv', encoding="utf-16le") 

# most visits are very short (consisting of few actions)
orgdf.actions.describe()

# here is a basic histogram
plt.hist(orgdf['actions'], bins=76)
plt.show()

orgdf.referrerName.unique()
orgdf['referrerName'] = orgdf['referrerName'].fillna('none')

# actions by referrer
tmpdf = orgdf[(orgdf['referrerName']=='Google') | 
              (orgdf['referrerName']=='none')]
tmp = pd.pivot_table(tmpdf, values='actions', index=['referrerName'],
                       aggfunc=['count',np.mean,np.median,np.max])

print(tmp)
# mean action when coming directly to the website (3.9) is 
# significantly higher  when compared to those coming from google (2.5)
# but the median is the same


# now let's import the stacked df
# basically is a combination of visit & action
jendf = pd.read_csv('stacked_df_02.csv') 

# replace zero with nan in all action columns
selection= jendf.loc[:0, 'type_of_action':'pageLoadTimeMilliseconds_of_action'].columns  # retrieve only the 0th row for efficiency
jendf[selection] = jendf[selection].replace({'0':np.nan, 0:np.nan})

# drop where all action columns are n/a
jendf = jendf.dropna(subset=selection, how='all')

# now we have a df of only relevant actions
tmp = pd.pivot_table(jendf, values='idVisit', index=['type_of_action'],
                       aggfunc='count')
print(tmp)
# most actions are actions, some are goals or outlinks, very few are downloads

# check conversions in original table
tmp = pd.pivot_table(orgdf, values='actions', index=['goalConversions'],
                       aggfunc='count')
# this corresponds to the number of goal actions

# let's select the last action only
jendf['action_wo_zero'] = jendf['action_number']+1
lastdf = jendf[jendf['actions']==jendf['action_wo_zero']]

tmp = pd.pivot_table(lastdf, values='idVisit', index=['type_of_action'],
                       aggfunc='count')
print(tmp)
# only 10% of all captured actions are outlinks
# but 24% of last actions are outlinks

# how fast do sessions end based on what is last action
tmp = pd.pivot_table(lastdf, values='action_wo_zero', index=['type_of_action'],
                       aggfunc=np.mean)
print(tmp)

lastdf.action_wo_zero.describe()


# then we can maybe look at this by referrer
tmpdf = lastdf[(lastdf['referrerName']=='Google') | 
              (lastdf['referrerName']=='0')]
tmp = pd.pivot_table(tmpdf, values='action_wo_zero', index=['type_of_action'],
                       columns=['referrerName'],aggfunc='count')
print(tmp)


# lets take a look at all actions that are outlinks
outlinks = jendf[jendf['type_of_action']=='outlink']

tmp = pd.pivot_table(outlinks, values='action_wo_zero', 
                     index=['url_of_action'],aggfunc='count').reset_index()

tmp = tmp.sort_values(by='action_wo_zero', ascending=False)
print(tmp.head(10))

# the how many-th action is the first outlink
# so for each visit id we grab the minimum action_number

min_outlinks = pd.pivot_table(outlinks, values='action_wo_zero', 
                     index=['idVisit'],aggfunc=np.min).reset_index()

min_outlinks.action_wo_zero.describe()

count_outlinks = pd.pivot_table(outlinks, values='action_wo_zero', 
                     index=['idVisit'],aggfunc='count').reset_index()

count_outlinks.action_wo_zero.describe()

plt.hist(count_outlinks['action_wo_zero'], bins=5)
plt.show()

#sessions with more than one outlink

oneplus_outlink = count_outlinks[count_outlinks['action_wo_zero']>=2]


