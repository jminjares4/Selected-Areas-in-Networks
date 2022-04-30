# !/bin/bash

# Jesus Minjares 
# Assignment 4 bash script

# Add switch flows

# Switch 1 configuration
sudo ovs-ofctl add-flow s1 arp,actions=normal
sudo ovs-ofctl add-flow s1 dl_dst=00:00:00:00:00:01,actions=output:1
sudo ovs-ofctl add-flow s1 dl_dst=00:00:00:00:00:02,actions=output:2
sudo ovs-ofctl add-flow s1 dl_dst=00:00:00:01:01:00,actions=output:3

# Switch 2 configuration
sudo ovs-ofctl add-flow s2 arp,actions=normal
sudo ovs-ofctl add-flow s2 dl_dst=00:00:00:00:00:03,actions=output:1
sudo ovs-ofctl add-flow s2 dl_dst=00:00:00:00:00:04,actions=output:2
sudo ovs-ofctl add-flow s2 dl_dst=00:00:00:02:02:00,actions=output:3

# Set gateway mac address
# Switch 3 configuration
sudo ovs-ofctl add-flow s3 arp,actions=normal
sudo ovs-ofctl add-flow s3 ip,nw_dst=192.168.1.11,actions=mod_dl_dst=00:00:00:00:00:01,output:1
sudo ovs-ofctl add-flow s3 ip,nw_dst=192.168.1.12,actions=mod_dl_dst=00:00:00:00:00:02,output:1
sudo ovs-ofctl add-flow s3 ip,nw_dst=192.168.2.13,actions=mod_dl_dst=00:00:00:00:00:03,output:2
sudo ovs-ofctl add-flow s3 ip,nw_dst=192.168.2.14,actions=mod_dl_dst=00:00:00:00:00:04,output:2