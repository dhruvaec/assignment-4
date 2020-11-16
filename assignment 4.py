#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Questions 1:
# How to import pandas and check the version?
import pandas as pd
print(pd.__version__)

# Output :
# 1.1.4
# 
# Process finished with exit code 0


# In[11]:


# Questions 2:
# How to create a series from a numpy array?

import numpy as np

import pandas as pd

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 91, 2, 4, 5, 8, 9, 6, 5, 4, 3, 2, 5])
print("Array of numpy is :", arr)

print("Series of pandas is :", pd.Series(arr))

# Output :
# Array of numpy is : [ 1  2  3  4  5  6  7  8 91  2  4  5  8  9  6  5  4  3  2  5]
# Series of pandas is : 0      1
# 1      2
# 2      3
# 3      4
# 4      5
# 5      6
# 6      7
# 7      8
# 8     91
# 9      2
# 10     4
# 11     5
# 12     8
# 13     9
# 14     6
# 15     5
# 16     4
# 17     3
# 18     2
# 19     5
# dtype: int64

# Process finished with exit code 0


# In[12]:


# Questions 3:
# How to convert the index of a series into a column of a dataframe ?

import pandas as pd

my_series = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9])
print("Series is :", my_series)

print("index of a series into a column of a data frame :", my_series.to_frame().reset_index())


# Output :
# /home/yogi/Desktop/Python_Code/venv/bin/python /home/yogi/Desktop/Python_Code/Lets_Upgrade_Assignments/Day4/Day4_Que3.py
# Series is :
# 0     1
# 1     2
# 2     3
# 3     4
# 4     5
# 5     6
# 6     7
# 7     8
# 8     9
# 9     3
# 10    4
# 11    5
# 12    6
# 13    7
# 14    8
# 15    9
# 16    2
# 17    3
# 18    4
# 19    5
# 20    6
# 21    7
# 22    8
# 23    9
# dtype: int64
# index of a series into a column of a data frame :     index  0
# 0       0  1
# 1       1  2
# 2       2  3
# 3       3  4
# 4       4  5
# 5       5  6
# 6       6  7
# 7       7  8
# 8       8  9
# 9       9  3
# 10     10  4
# 11     11  5
# 12     12  6
# 13     13  7
# 14     14  8
# 15     15  9
# 16     16  2
# 17     17  3
# 18     18  4
# 19     19  5
# 20     20  6
# 21     21  7
# 22     22  8
# 23     23  9
#
# Process finished with exit code 0


# In[7]:


# Questions 4:
# Write the code to list all the datasets available in seaborn library.
# Load the 'mpg' dataset
# Note: mpg dataset will be read from seaborn module in the manner sir has already shown(provided in the
# materials folder)
import seaborn as sns
import pandas as pd
print("All dataset present in the seaborn library :", sb.get_dataset_names()) # list of all dataset in the seaborn
print()

mpg = sb.load_dataset('mpg')
print("mpg data set from seaborn :", mpg) # loading mpg data set from seaborn library
print()
print("'anagrams' data set from seaborn :", sb.load_dataset('anagrams'))
print()
print("car_crashes data set from seaborn :", sb.load_dataset('car_crashes'))
print()
print(pd.read_csv("student_records.csv")) # loading user data set using pandas library


# Output :
# /home/yogi/Desktop/Python_Code/venv/bin/python /home/yogi/Desktop/Python_Code/Lets_Upgrade_Assignments/Day4/Day4_Que4.py
# All dataset present in the seaborn library : ['anagrams', 'anscombe', 'attention',
# 'brain_networks', 'car_crashes', 'diamonds', 'dots', 'exercise', 'flights', 'fmri',
# 'gammas', 'geyser', 'iris', 'mpg', 'penguins', 'planets', 'tips', 'titanic']
#
# mpg data set from seaborn :       mpg  cylinders  ...  origin                       name
# 0    18.0          8  ...     usa  chevrolet chevelle malibu
# 1    15.0          8  ...     usa          buick skylark 320
# 2    18.0          8  ...     usa         plymouth satellite
# 3    16.0          8  ...     usa              amc rebel sst
# 4    17.0          8  ...     usa                ford torino
# ..    ...        ...  ...     ...                        ...
# 393  27.0          4  ...     usa            ford mustang gl
# 394  44.0          4  ...  europe                  vw pickup
# 395  32.0          4  ...     usa              dodge rampage
# 396  28.0          4  ...     usa                ford ranger
# 397  31.0          4  ...     usa                 chevy s-10
#
# [398 rows x 9 columns]
#
# 'anagrams' data set from seaborn :     subidr    attnr  num1  num2  num3
# 0        1  divided     2   4.0     7
# 1        2  divided     3   4.0     5
# 2        3  divided     3   5.0     6
# 3        4  divided     5   7.0     5
# 4        5  divided     4   5.0     8
# 5        6  divided     5   5.0     6
# 6        7  divided     5   4.5     6
# 7        8  divided     5   7.0     8
# 8        9  divided     2   3.0     7
# 9       10  divided     6   5.0     6
# 10      11  focused     6   5.0     6
# 11      12  focused     8   9.0     8
# 12      13  focused     6   5.0     9
# 13      14  focused     8   8.0     7
# 14      15  focused     8   8.0     7
# 15      16  focused     6   8.0     7
# 16      17  focused     7   7.0     6
# 17      18  focused     7   8.0     6
# 18      19  focused     5   6.0     6
# 19      20  focused     6   6.0     5
#
# car_crashes data set from seaborn :     total  speeding  alcohol  ...  ins_premium  ins_losses  abbrev
# 0    18.8     7.332    5.640  ...       784.55      145.08      AL
# 1    18.1     7.421    4.525  ...      1053.48      133.93      AK
# 2    18.6     6.510    5.208  ...       899.47      110.35      AZ
# 3    22.4     4.032    5.824  ...       827.34      142.39      AR
# 4    12.0     4.200    3.360  ...       878.41      165.63      CA
# 5    13.6     5.032    3.808  ...       835.50      139.91      CO
# 6    10.8     4.968    3.888  ...      1068.73      167.02      CT
# 7    16.2     6.156    4.860  ...      1137.87      151.48      DE
# 8     5.9     2.006    1.593  ...      1273.89      136.05      DC
# 9    17.9     3.759    5.191  ...      1160.13      144.18      FL
# 10   15.6     2.964    3.900  ...       913.15      142.80      GA
# 11   17.5     9.450    7.175  ...       861.18      120.92      HI
# 12   15.3     5.508    4.437  ...       641.96       82.75      ID
# 13   12.8     4.608    4.352  ...       803.11      139.15      IL
# 14   14.5     3.625    4.205  ...       710.46      108.92      IN
# 15   15.7     2.669    3.925  ...       649.06      114.47      IA
# 16   17.8     4.806    4.272  ...       780.45      133.80      KS
# 17   21.4     4.066    4.922  ...       872.51      137.13      KY
# 18   20.5     7.175    6.765  ...      1281.55      194.78      LA
# 19   15.1     5.738    4.530  ...       661.88       96.57      ME
# 20   12.5     4.250    4.000  ...      1048.78      192.70      MD
# 21    8.2     1.886    2.870  ...      1011.14      135.63      MA
# 22   14.1     3.384    3.948  ...      1110.61      152.26      MI
# 23    9.6     2.208    2.784  ...       777.18      133.35      MN
# 24   17.6     2.640    5.456  ...       896.07      155.77      MS
# 25   16.1     6.923    5.474  ...       790.32      144.45      MO
# 26   21.4     8.346    9.416  ...       816.21       85.15      MT
# 27   14.9     1.937    5.215  ...       732.28      114.82      NE
# 28   14.7     5.439    4.704  ...      1029.87      138.71      NV
# 29   11.6     4.060    3.480  ...       746.54      120.21      NH
# 30   11.2     1.792    3.136  ...      1301.52      159.85      NJ
# 31   18.4     3.496    4.968  ...       869.85      120.75      NM
# 32   12.3     3.936    3.567  ...      1234.31      150.01      NY
# 33   16.8     6.552    5.208  ...       708.24      127.82      NC
# 34   23.9     5.497   10.038  ...       688.75      109.72      ND
# 35   14.1     3.948    4.794  ...       697.73      133.52      OH
# 36   19.9     6.368    5.771  ...       881.51      178.86      OK
# 37   12.8     4.224    3.328  ...       804.71      104.61      OR
# 38   18.2     9.100    5.642  ...       905.99      153.86      PA
# 39   11.1     3.774    4.218  ...      1148.99      148.58      RI
# 40   23.9     9.082    9.799  ...       858.97      116.29      SC
# 41   19.4     6.014    6.402  ...       669.31       96.87      SD
# 42   19.5     4.095    5.655  ...       767.91      155.57      TN
# 43   19.4     7.760    7.372  ...      1004.75      156.83      TX
# 44   11.3     4.859    1.808  ...       809.38      109.48      UT
# 45   13.6     4.080    4.080  ...       716.20      109.61      VT
# 46   12.7     2.413    3.429  ...       768.95      153.72      VA
# 47   10.6     4.452    3.498  ...       890.03      111.62      WA
# 48   23.8     8.092    6.664  ...       992.61      152.56      WV
# 49   13.8     4.968    4.554  ...       670.31      106.62      WI
# 50   17.4     7.308    5.568  ...       791.14      122.04      WY
#
# [51 rows x 8 columns]
#
#      Name OverallGrade Obedient  ResearchScore  ProjectScore Recommend
# 0   Henry            A        Y             90            85       Yes
# 1    John            C        N             85            51       Yes
# 2   David            F        N             10            17        No
# 3  Holmes            B        Y             75            71        No
# 4  Marvin            E        N             20            30        No
# 5   Simon            A        Y             92            79       Yes
# 6  Robert            B        Y             60            59        No
# 7   Trent            C        Y             75            33        No
#
# Process finished with exit code 0


# In[8]:


# Questions 4:
# Write the code to list all the datasets available in seaborn library.
# Load the 'mpg' dataset
# Note: mpg dataset will be read from seaborn module in the manner sir has already shown(provided in the
# materials folder)
import seaborn as sns
import pandas as pd
print("All dataset present in the seaborn library :", sb.get_dataset_names()) # list of all dataset in the seaborn
print()

mpg = sb.load_dataset('mpg')
print("mpg data set from seaborn :", mpg) # loading mpg data set from seaborn library
print()
print("'anagrams' data set from seaborn :", sb.load_dataset('anagrams'))
print()
print("car_crashes data set from seaborn :", sb.load_dataset('car_crashes'))
print()
print(pd.read_csv("student_records.csv")) # loading user data set using pandas library


# In[1]:


# Questions 5:
# Which country origin cars are a part of this dataset?

import seaborn as sb
import pandas as pd
data_set = sb.load_dataset('mpg')
print(data_set)

df = pd.DataFrame(data_set)
print(" country origin :", df.origin.unique())

# Output :
# /home/yogi/Desktop/Python_Code/venv/bin/python /home/yogi/Desktop/Python_Code/
# Lets_Upgrade_Assignments/Day4/Day4_Que5.py
#       mpg  cylinders  ...  origin                       name
# 0    18.0          8  ...     usa  chevrolet chevelle malibu
# 1    15.0          8  ...     usa          buick skylark 320
# 2    18.0          8  ...     usa         plymouth satellite
# 3    16.0          8  ...     usa              amc rebel sst
# 4    17.0          8  ...     usa                ford torino
# ..    ...        ...  ...     ...                        ...
# 393  27.0          4  ...     usa            ford mustang gl
# 394  44.0          4  ...  europe                  vw pickup
# 395  32.0          4  ...     usa              dodge rampage
# 396  28.0          4  ...     usa                ford ranger
# 397  31.0          4  ...     usa                 chevy s-10
#
# [398 rows x 9 columns]
#  country origin : ['usa' 'japan' 'europe']
#
# Process finished with exit code 0


# In[2]:


# Questions 6:
# Extract the part of the dataframe which contains cars belonging to 'usa'

import seaborn as sb
import pandas as pd

data_set = sb.load_dataset('mpg')
print(data_set)

df = pd.DataFrame(data_set)

print(" Data set extracted only for usa :", df[df['origin'].str.contains("usa")])

# Output :
# /home/yogi/Desktop/Python_Code/venv/bin/python /home/yogi/Desktop/Python_Code/
# Lets_Upgrade_Assignments/Day4/Day4_Que6.py
#       mpg  cylinders  ...  origin                       name
# 0    18.0          8  ...     usa  chevrolet chevelle malibu
# 1    15.0          8  ...     usa          buick skylark 320
# 2    18.0          8  ...     usa         plymouth satellite
# 3    16.0          8  ...     usa              amc rebel sst
# 4    17.0          8  ...     usa                ford torino
# ..    ...        ...  ...     ...                        ...
# 393  27.0          4  ...     usa            ford mustang gl
# 394  44.0          4  ...  europe                  vw pickup
# 395  32.0          4  ...     usa              dodge rampage
# 396  28.0          4  ...     usa                ford ranger
# 397  31.0          4  ...     usa                 chevy s-10
#
# [398 rows x 9 columns]
#  Data set extracted only for usa :
# mpg  cylinders  ...         origin               name
# 0    18.0          8  ...     usa  chevrolet chevelle malibu
# 1    15.0          8  ...     usa          buick skylark 320
# 2    18.0          8  ...     usa         plymouth satellite
# 3    16.0          8  ...     usa              amc rebel sst
# 4    17.0          8  ...     usa                ford torino
# ..    ...        ...  ...     ...                        ...
# 392  27.0          4  ...     usa           chevrolet camaro
# 393  27.0          4  ...     usa            ford mustang gl
# 395  32.0          4  ...     usa              dodge rampage
# 396  28.0          4  ...     usa                ford ranger
# 397  31.0          4  ...     usa                 chevy s-10
#
# [249 rows x 9 columns]
#
# Process finished with exit code 0


# In[ ]:




