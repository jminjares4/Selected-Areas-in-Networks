# !/bin/bash

# Jesus Minjares 
# Assignment 4 bash script

# add switchs flow

# Switch 1
sudo ovs-ofctl add-flow sl arp,actions-normal
sudo ovs-ofctl add-flow sl d1_dst=00:00:00:00:00:01,actions=output:1
sudo ovs-ofctl add-flow sl dl_dst=00:00:00:00:00:02,actions=output:2
sudo ovs-ofctl add-flow sl d1_dst=00:00:00:00:01:01,actions=output:3

# Switch 2
sudo ovs-ofctl add-flow s2 arp,actions-normal
sudo ovs-ofcti add-flow s2 d1_dst=00:00:00:00:00:03,actions=output:1
sudo ovs-ofctl add-flow s2 d1_dst=00:00:00:00:00:04,actions=output:2
sudo ovs-ofctl add-flow s2 d1_dst=00:00:00:00:02:02,actions=output:3

# Switch 3
sudo ovs-ofcti add-flow s3 arp, actions-normal
sudo ovs-ofctl add-flow s3 ip,nw_dst=192.168.1.11,actions=mod_d1_dst=00:00:00:00:00:01,output:1
sudo ovs-ofctl add-flow s3 ip,nw_dst=192.168.1.12,actions=mod_d1_dst=00:00:00:00:00:02,output:2
sudo ovs-ofctl add-flow s3 ip,nw_dst=192.168.1.13,actions=mod_d1_dst=00:00:00:00:00:03,output:3
sudo ovs-ofctl add-flow s3 ip,nw_dst=192.168.1.14,actions=mod_d1_dst=00:00:00:00:00:04,output:4

# Hard code gateway mac and ip address 
# ip route add default via 192.168.1.1
# arp -s 192.168.1.1 00:00:00:00:01:01
# arp -s 192.168.1.12 00:00:00:00:00:02

# ip route add default via 192.168.1.1
# arp -s 192.168.1.1 00:00:00:00:01:01
# arp -s 192.168.1.11 00:00:00:00:00:01

# ip route add default via 192.168.2.1
# arp -s 192.168.2.1 00:00:00:00:02:02
# arp -s 192.168.2.14 00:00:00:00:00:04

# ip route add default via 192.168.2.1
# arp -s 192.168.2.1 00:00:00:00:02:02
# arp -s 192.168.2.13 00:00:00:00:00:03