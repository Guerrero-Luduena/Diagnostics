
# coding: utf-8

# In[3]:

import pandas as pd
import numpy as np
import zipfile
from os import listdir
from os.path import isfile, join


# ## UnZip files

# In[5]:

#### specify directory that you want unzipping
directory = '../diag_data/Monthly_Diagnostic_Waiting_Times_and_Activity/'


# In[6]:

#### get list of files in directory
files = [f for f in listdir(directory) if isfile(join(directory, f))]

#### filter for .zip files
files = [x for x in files if x.endswith(('.zip'))]


# In[8]:

#### unzip all files in 'directory' with same names as .zip files
for file in files:
    z = zipfile.ZipFile(directory + file)
    for i, f in enumerate(z.filelist):
        filename_noext = file.split('.')[0]
        old_ext = f.filename.split('.')[-1]
        f.filename = (filename_noext + '.' + old_ext).format(i)
    z.extract(f, path=directory)


# ## Begin combining files

# In[ ]:




# # Dev

# In[1]:

directory = '../diag_data/test/'


# In[5]:

#### get list of files in directory
files = [f for f in listdir(directory) if isfile(join(directory, f))]

#### filter for .csv files
files = [x for x in files if x.endswith(('.csv'))]


# In[7]:

files


# In[39]:

master = pd.DataFrame()
for name in files:
    #### make temp df with new csv
    temp = pd.read_csv(directory + name , skiprows=4)
    
    #### get timestamp
    time_id = name.split('(')[-1]
    time_id = time_id.split(')')[0]
    print(time_id)
    ##comvert to datetime
    time_id = pd.to_datetime(time_id)
    
    #### add year.month column
    year_month = time_id.strftime('%Y.%m') # create value
    temp['Year_month'] = year_month # create new column and impute values
    temp['year1'] = time_id.strftime('%Y')
    temp['month'] = time_id.strftime('%m')
    
    
    #### append current temp df to master df
    master = master.append(temp, ignore_index=True)


# In[40]:

master.head()


# In[29]:

pd.to_datetime(time_id).strftime('%Y.%m')


# In[ ]:

names = pd.DataFrame()
for year in years:
    path ='C:\\Documents and Settings\\Foo\\My Documents\\pydata-book\\pydata-book-master`\\ch02\\names\\yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)

    frame['year'] = year
    names = names.append(frame, ignore_index=True)

