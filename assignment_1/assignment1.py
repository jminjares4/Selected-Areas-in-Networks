# Author: Jesus Minjares
# Assignment 1:
"""
Write a python script that plots the queueing delay (y-axis) vs the average arrival 
rate (x-axis) for the system in question 6. The range should be from 0.1 Mbp

* Reference question
6. What is the average waiting time in the queue (i.e., queueing delay) if the arrival rate to 
that queue follows an exponential distribution with an average rate of 1.7 Mbps and that 
queue is served by a transmission channel with a 2 Mbps rate?

"""
# Date: 02-02-2022

# import necessary packages
import numpy as np 
import matplotlib.pyplot as plt

# create function to get queueing delay
queue_delay = lambda l,u: l/(2*(u**2) *(1 - l/u))

# 0.1->1.90 Mbps for arrival time
arrival = np.arange(.1,1.90,.001) 

# store queue delay of the arrival time into queue using list comprehension
queue = [queue_delay(i,2) for i in arrival]

# Plot
# set x->arrival, y-<queue, color as blue, set label
plt.plot(arrival,queue,color='blue',label='Exponential Distribution',linewidth=2.5)
# add x and y labels
plt.xlabel('Average Arrival Rate (Mbps)', fontsize=10, fontweight='bold')
plt.ylabel('Queueing Delay (s)', fontsize=10, fontweight='bold')
# reset xticks intervals
plt.xticks(np.arange(0.1, 1.91, 0.2))
# set margin to 2%
plt.margins(0.02)
# add title 
plt.title('Queueing Delay vs Average Arrival Rate', fontweight='bold')
# add legend
plt.legend(loc='best')
# display plot
plt.show()

