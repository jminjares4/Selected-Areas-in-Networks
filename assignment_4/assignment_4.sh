# !/bin/bash

# Jesus Minjares 
# Assignment 4 bash script

# add switchs flow

# Switch 1
sudo ovs-ofctl add-flow sl arp, actions-normal
sudo ovs-ofctl add-flow sl d1 dst=00:00:00:00:00:01,actions=output:1
sudo ovs-ofctl add-flow sl dl dst=00:00:00:00:00:02,actions=output:2
sudo ovs-ofctl add-flow sl d1 dst=00:00:00:00:01:01,actions=output:3

# Switch 2
sudo ovs-ofctl add-flow s2 arp, actions-normal
sudo ovs-ofcti add-flow s2 d1 dst=00:00:00:00:00:03,actions=output:1
sudo ovs-ofctl add-flow s2 d1 dst=00:00:00:00:00:04,actions=output:2
sudo ovs-ofctl add-flow s2 d1 dst=00:00:00:00:02:02,actions=output:3

# Switch 3
sudo ovs-ofcti add-flow s3 arp, actions-normal
sudo ovs-ofctl add-flow s3 ip,nw dst=192.168.1.11,,actions=mod d1 dst=00:00:00:00:00:01,output:1
sudo ovs-ofctl add-flow s3 ip,nw dst=192.168.1.12,,actions=mod d1 dst=00:00:00:00:00:02,output:2
sudo ovs-ofctl add-flow s3 ip,nw dst=192.168.1.13,,actions=mod d1 dst=00:00:00:00:00:03,output:3
sudo ovs-ofctl add-flow s3 ip,nw dst=192.168.1.14,,actions=mod d1 dst=00:00:00:00:00:04,output:4
