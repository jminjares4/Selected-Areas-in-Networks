# Author: Jesus Minjares
# Assignment 3B:
"""
   Add four colums to your original PANDAS dataframe from 4) called 'src_as', 'src_org', 
  'dst_as', 'dst_org' using the data in the 'as.csv' file. Submit your Python script through 
  Blackboard named lastname_3b.py.  
"""
# Data: 02-21-2022

from unittest import skip
import pandas as pd
import sys
import ipaddress as ip

# def decimal_value(ip:str) -> int:
#     """Convert IPV4 IP Address to decimal"""
#     if ":" in ip:
#       return 0 # avoid masking ipv6
#     else:
#       ip_address = ip.split('.')
#       return int(ip_address[0]) << 24 | int(ip_address[1]) << 16 | int(ip_address[2])  << 8 | int(ip_address[3]) << 0
    
# def func(value, test):
#     try:
#       value = (ip.ip_address(value))
#       if value > ip.ip_address(test['startIP']) and value < ip.ip_address(test['endIP']):
#         return test['asNum']
#       else:
#         return NaN
#     except ValueError:
#       return 0

def func(row, df_as):
   return df_as.apply( lambda row_as: row_as['asNum'] (row) > df_as['startIP'] and (row) < df_as['endIP'])
def match_asNum(row, df):
    try:
      row = df.apply(lambda x: row >= int(ip.ip_address(x['startIP'])) and row <= int(ip.ip_address(x['endIP'])))
    except ValueError:
      return 0
def func(row, df_as):
   return df_as.apply( lambda row_as: row_as['asNum'] (row) > df_as['startIP'] and (row) < df_as['endIP'])

if __name__=="__main__":
  if len(sys.argv) < 3:
    # output message
    print('Usage: python3 minjares_3a.py file.csv as.csv')
  else:
    # store csv file into a data frame 
    df = pd.read_csv(sys.argv[1])
    df_as = pd.read_csv(sys.argv[2])

    column_names = ["src_as", "src_org", "dst_as", "dst_org"]
    temp_df = pd.DataFrame(columns = column_names)

    df = pd.concat([df, temp_df], axis=0, ignore_index=True)
  
    src_ip_unique = df['SRC_IP'].unique()
    dst_ip_unique = df['DST_IP'].unique()

    
    data = df.isin()