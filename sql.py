# import numpy as np 
import pandas as pd
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
import pandas as pd
import sqlite3

## Read the file
df = pd.read_csv('zomato.csv')

## print the columns of all dataframes
print('The columns of the zomato data frame are :-  ',df.columns)

# import sqlalchemy and create a sqlite engine
from sqlalchemy import create_engine
engine = create_engine('sqlite://', echo=False)

# export the dataframe as a table 'playstore' to the sqlite engine
df.to_sql("zomato", con =engine)