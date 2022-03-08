# Author: Jesus Minjares
# Assignment 3B:
"""
   Add four colums to your original PANDAS dataframe from 4) called 'src_as', 'src_org', 
  'dst_as', 'dst_org' using the data in the 'as.csv' file. Submit your Python script through 
  Blackboard named lastname_3b.py.  
"""
# Data: 02-28-2022

import pandas as pd
import sys
import ipaddress as ip


def filter_tcp(data):
  """Filter TCP data that exceeed 100 byte in the dataframe"""
  tcp_data = data[ (data['PROTOCOL'] == 'tcp') & (data['BYTES'] > 100) ]
  return tcp_data

if __name__=="__main__":
  if len(sys.argv) < 3:
    # output message
    print('Usage: python3 minjares_3a.py netflow.csv as.csv')
  else:
    # store csv file into a data frame 
    df = pd.read_csv(sys.argv[1])
    df_as = pd.read_csv(sys.argv[2])

    df = filter_tcp(df)
    # filter the data frame by tcp protcol that is greater than 100 bytes
    # df = df[ (df['PROTOCOL'] == 'tcp') & (df['BYTES'] > 100) ]

    # add additional columns to the data frame
    column_names = ["src_as", "src_org", "dst_as", "dst_org"]

    # create temporary data frame to store column
    temp_df = pd.DataFrame(columns = column_names)

    # concatenate both dataframes
    df = pd.concat([df, temp_df], axis=0, ignore_index=True)

    # sort to ascending
    df = df.sort_values(by='SRC_IP', ascending=True)

    # quick test
    df = df.head(15)

    # Brute Force
    """
    The follow section of the code is the brute version algorithm. 
    It will iterate over all rows of netflow file and as.csv, the software was 
    verify using df.head() as input. However, the implemention is too slows as the 
    time complexity will O(n^2) and the total lines of as.csv is 430327.

    TODO:
        Change the brute force algorithm with vectorized operations using
        pandas builtin methods. For instance use apply, merge and concat to
        manipulate the data. 
    """
    i  = 0
    for index, row in df.iterrows(): # iterate over all the rows 
      # store ip_address mask
      ip_address_src = int(ip.ip_address(row['SRC_IP']))
      ip_address_dst = int(ip.ip_address(row['DST_IP']))
      for index2, as_row in df_as.iterrows():
        # check if start_ip < src < end_ip 
        if ip_address_src >= int(ip.ip_address(as_row['startIP'])) and ip_address_src <= int(ip.ip_address(as_row['endIP'])):
          # store asNum and organization
          df.at[i,'src_as'] = int((as_row['asNum']))
          df.at[i,'src_org'] = str((as_row['organization']))

        # check if start_ip < dst < end_ip 
        if ip_address_dst >= int(ip.ip_address(as_row['startIP'])) and ip_address_dst <= int(ip.ip_address(as_row['endIP'])):
          # store asNum and organization
          df.at[i,'dst_as'] = int((as_row['asNum']))
          df.at[i,'dst_org'] = str((as_row['organization']))
      i = i + 1 # increase index

    print(df.head(5)) # verify that the columns have been updated
