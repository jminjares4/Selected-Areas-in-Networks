# Author: Jesus Minjares
# Assignment 3A:
"""
  Capture flow data with pmacct to a CSV file. Write a python script that loads the flow 
  data into a PANDAS dataframe. Create a new dataframe that is a subset of the original 
  data frame using PANDAS to isolate the TCP flows where the number of flow bytes 
  exceeds 100. Submit this python script through Blackboard named lastname_3a.py. 
"""
# Data: 02-28-2022

import pandas as pd
import sys

if __name__=="__main__":
  if len(sys.argv) < 2:
    # output message
    print('Usage: python3 minjares_3a.py file.csv')
  else:
    # store csv file into a data frame 
    data = pd.read_csv(sys.argv[1])

    # filter the data frame by tcp protcol that is greater than 100 bytes
    tcp_data = data[ (data['PROTOCOL'] == 'tcp') & (data['BYTES'] > 100) ]

    # verify all column are csv and match the count
    print(tcp_data.duplicated(['PROTOCOL']).count() == tcp_data['PROTOCOL'].count()) 
    