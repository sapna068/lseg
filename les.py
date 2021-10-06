
# coding: utf-8

# In[1]:



import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
import matplotlib
get_ipython().magic('matplotlib inline')
import warnings
warnings.filterwarnings('ignore')


# In[58]:


df = pd.read_csv("lsegdata.csv")
df.head()


# In[59]:


df.describe()


# In[60]:


df.info()


# In[18]:


df['account_number'].value_counts()


# In[61]:


df.isnull().sum()


# In[62]:


df['amount'] = df['amount'].fillna(df['amount'].mean())


# In[63]:


df['transaction_type`'] = df["transaction_type`"].fillna(df['transaction_type`'].mode()[0])


# In[64]:


df.isnull().sum()


# In[65]:


#df.drop(labels='description(of txn)', axis=1)


# In[66]:


df.isnull().sum()


# In[69]:


# label encoding
df.replace({"transaction_type":{'debit':0,'credit':1}},inplace=True)


# In[70]:


df.head()


# In[71]:


gkk = df.groupby(['bank_account id', 'account_number'])


# In[72]:


gkk.first()


# In[78]:


df.groupby(['bank_account id', 'account_number']).size().reset_index(name='counts')


# In[84]:


from sklearn import preprocessing


# In[85]:


label_Encoder=preprocessing.LabelEncoder()


# In[88]:


# label encoding
df.replace({"transaction_type`":{'debit':0,'credit':1}},inplace=True)


# In[89]:


df.head()


# In[95]:


df.groupby(['transaction_type`']).size().reset_index(name='counts')


# In[96]:


df.groupby(['bank_account id', 'transaction_type`']).size().reset_index(name='counts')


# In[97]:


df.groupby('transaction_type`').mean()


# In[ ]:


#drop unwanted columns:description

