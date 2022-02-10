# Author: Jesus Minjarse
# Assignment 2:
"""
Capture flow data with pmacct to a CSV file. Write a python script to load the CSV file 
into a PANDAS dataframe, print the minimum and maximum number of flow bytes, and 
plot the histogram of flow bytes; all with PANDAS functions (use v1.4 of PANDAS). I 
want to see a lot of detail in the histogram so do not use the default number of bins, use 
many more. Hint: use column='BYTES' as one of the arguments to the hist() function to 
get it to work correctly.
"""
# Data: 02-09-2022

# import pandas and matplotlib packages 
import pandas as pd
import matplotlib.pyplot as plt
import sys

if __name__=="__main__":
    if len(sys.argv) < 2:
        print('Usage: python3 assignment2.py file.csv')
    else:
        # store argument into variable
        my_file = str(sys.argv[1])

        # Store csv file into a data frame
        data = pd.read_csv(my_file)

        # get the min and max value for 'BYTES' column of the data frame
        min_val, max_val = min(data['BYTES']) , max(data['BYTES'])

        # get the min and max value for the frequency of the packets
        y_min, y_max = min(data['BYTES'].value_counts()), max(data['BYTES'].value_counts())

        # create a histogram using pandas.DataFrame.hist for 'BYTES' with 400 bins 
        data_frame_graph = pd.DataFrame.hist(data, column='BYTES',grid=False,bins=400,range=[min_val,max_val],
                                        label='Bytes', xlabelsize=10, ylabelsize=10, color='midnightblue')
        # Add title
        plt.title('Histogram of Bytes in NetFlow', fontweight='bold')

        # set xlabel
        plt.xlabel('Packets (BYTES)')
        # set ylabel
        plt.ylabel('Frequency')
        # display legend
        plt.legend()
        # add text @ the middle of the histogram
        plt.text(max_val/2, y_max/2,f'Min: {min_val}\nMax: {max_val}')
        # save figure
        plt.savefig('assignment_2_hist.png')
        # display graph
        plt.show()

