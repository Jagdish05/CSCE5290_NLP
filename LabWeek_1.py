#!/usr/bin/env python
# coding: utf-8

# In[1]:


import urllib.request
response = urllib.request.urlopen('https://www.spacex.com')
html = response.read()
print(html)


# ### Use BeautifulSoup to clean the grabbed text like 

# In[2]:


from bs4 import BeautifulSoup
soup = BeautifulSoup(html,"html5lib")

text = soup.get_text(strip=True)
print(text)


# ### Clean text from the crawled web page

# In[3]:


tokens = [t for t in text.split()]
print(tokens)


# ### Count word frequency

# In[5]:


import nltk
freq = nltk.FreqDist(tokens)

for key,val in freq.items():

    print (str(key) + ':' + str(val))


# ### plot a graph for those tokens

# In[6]:


freq.plot(20, cumulative=False)


# ### Remove stop words using NLTK

# In[7]:


from nltk.corpus import stopwords
clean_tokens = tokens[:]

sr = stopwords.words('english')

for token in tokens:

    if token in sr:
        clean_tokens.remove(token)
print(clean_tokens)


# ### Plot graph with stopwords

# In[8]:


freq = nltk.FreqDist(clean_tokens)
freq.plot(10, cumulative=False)


# ### Created Bar graph

# In[43]:


import pandas as pd
df_fdist = pd.DataFrame.from_dict(freq, orient='index')
df_fdist.columns = ['Frequency']
df_fdist.index.name = 'Term'
# print(df_fdist)
df_fdist = df_fdist.sort_values(by=['Frequency'])
df_fdist=df_fdist[-10:]
print(df_fdist)
df_fdist.plot.bar()


# In[ ]:




