#!/usr/bin/env python
# coding: utf-8

# In[18]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('fivethirtyeight')
from datetime import datetime

import pandas_datareader.data as web


# In[19]:


#Get the stock starting date
stockStartDate = '2011-08-26'
# Get the stocks ending date aka todays date
#and format it in the form YYYY-MM-DD
today = datetime.today().strftime('%Y-%m-%d')


# In[20]:


#extract the closing price data
df=web.DataReader(['AMZN','GOOG','TSLA'],'yahoo',
                  start=stockStartDate,end=today)['Adj Close']


# In[21]:


#drop null values
df.dropna(inplace=True,axis=0)


# In[22]:


#store daily return of all above stocks in a new dataframe
chng_df=df.pct_change()*100
chng_df.dropna(inplace=True,axis=0)


# Analyse the correlation between the different stocks in a pair-wise fashion with seaborn pairplot

# In[23]:


#plotting pairplot
sns.set(style='ticks',font_scale=1.25)
sns.pairplot(chng_df)


# The correlation analysis is performe on the daily percentage change(daily returns) of the stock price and not the stock. price

# Takeaway:
# Amazon and Tesla stocks can be included in a portfolio as they do not show any significant correlation.

# Drawback:
# Although the pair plots provide very good visualization of all possible combinations between the bunch of stocks, it doesn’t provide any detailed information like Pearson’s R value or null-hypothesis p value to quantify the correlation. That’s where the joint plot comes into the picture!
# 

# In[25]:


from scipy.stats import stats
sns.jointplot('AMZN','TSLA',chng_df,kind='scatter').annotate(stats.pearsonr)

plt.show()


# Takeaways:
# The Pearson’s R value is 0.32 for Amazon v/s Tesla which is very less. This indicates a weak correlation.

# Next, we will calculate the 7-day rolling mean(also called moving average) of the daily returns, then compute the standard deviation (which is square root of the variance) and plot the values. Relax
# 
# 

# In[26]:


volatility=chng_df[['AMZN','GOOG','TSLA']].rolling(7).std()*np.sqrt(7)
volatility.plot(figsize=(15,7))


# You can observe that Tesla stock has higher volatility as compared to Google and Aamazon. This is expected as Tesla is a mid-cap stock and mid-cap stocks in general tend to have higher volatility as compared to the large-cap stocks such as Amazon.
# Many traders and investors seek out higher volatility investments in order to make higher profits. If a stock does not move, not only it has low volatility, but also it has low gain potential. On the other hand, a stock or other security with a very high volatility level can have tremendous profit potential, but the risk is equally high.
# 
# 

# In[ ]:




