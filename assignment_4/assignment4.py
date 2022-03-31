"""
Assignment 4 Python Script: Create a network that consists of 2 subnets joined
                            by switch. Each subnet will have a total of 2 hosts
                            and these hosts will be connected to the same switch,
                            which will interact with the hosts by using Layer 2
                            protocols. Both subnet's switches will be connected to
                            a third switch, which will use Layer 3 protocol.
                            The task is to be able to ping all of the hosts and test
                            the bandwidth of each of the host pairs successfully.
"""

# Import Mininet modules
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI

# Instantiate Mininet
net = Mininet()

# Create hosts, switches, remote controller, and links between hosts and switches.
h1 = net.addHost('h1', mac='00:00:00:00:00:01', ip='192.168.1.11', prefix=24)
h2 = net.addHost('h2', mac='00:00:00:00:00:02', ip='192.168.1.12', prefix=24)
h3 = net.addHost('h3', mac='00:00:00:00:00:03', ip='192.168.2.13', prefix=24)
h4 = net.addHost('h4', mac='00:00:00:00:00:04', ip='192.168.2.14', prefix=24)

# Add switches
s1 = net.addSwitch('s1')
s2 = net.addSwitch('s2')
s3 = net.addSwitch('s3')

# Add remote controller
net.addController('c0', controller=RemoteController)

# Link all components
# Link H1 -> S1
net.addLink('h1', 's1')
# Link H2 -> S1
net.addLink('h2', 's1')
# Link H3 -> S2
net.addLink('h3', 's2')
# Link H4 -> S2
net.addLink('h4', 's2')
# Link S1 -> S3
net.addLink('s1', 's3')
# Link S2 -> S3
net.addLink('s2', 's3')

# Start mininet network
net.start()

# s1
s1.cmd('ovs-ofctl add-flow s1 arp,actions=normal')
s1.cmd('ovs-ofctl add-flow s1 dl_dst=00:00:00:00:00:01,actions=output:1')
s1.cmd('ovs-ofctl add-flow s1 dl_dst=00:00:00:00:00:02,actions=output:2')
s1.cmd('ovs-ofctl add-flow s1 dl_dst=00:00:00:00:01:01,actions=output:3')

# s2
s2.cmd('ovs-ofctl add-flow s2 arp,actions-normal')
s2.cmd('ovs-ofcti add-flow s2 dl_dst=00:00:00:00:00:03,actions=output:1')
s2.cmd('ovs-ofctl add-flow s2 dl_dst=00:00:00:00:00:04,actions=output:2')
s2.cmd('ovs-ofctl add-flow s2 dl_dst=00:00:00:00:02:02,actions=output:3')

# s3
s3.cmd('ovs-ofctl add-flow s3 arp, actions-normal')
s3.cmd('ovs-ofctl add-flow s3 ip,nw_dst=192.168.1.11,actions=mod_dl_dst=00:00:00:00:00:01,output:1')
s3.cmd('ovs-ofctl add-flow s3 ip,nw_dst=192.168.1.12,actions=mod_dl_dst=00:00:00:00:00:02,output:1')
s3.cmd('ovs-ofctl add-flow s3 ip,nw_dst=192.168.2.13,actions=mod_dl_dst=00:00:00:00:00:03,output:2')
s3.cmd('ovs-ofctl add-flow s3 ip,nw_dst=192.168.2.14,actions=mod_dl_dst=00:00:00:00:00:04,output:2')


# Set gateway ip_address and mac_address

# H1 configuration
h1.cmd("ip route add default via 192.168.1.1")
h1.cmd("arp -s 192.168.1.1 00:00:00:00:01:01")
h1.cmd("arp -s 192.168.1.12 00:00:00:00:00:02")

# H2 configuration
h2.cmd("ip route add default via 192.168.1.1")
h2.cmd("arp -s 192.168.1.1 00:00:00:00:01:01")
h2.cmd("arp -s 192.168.1.11 00:00:00:00:00:01")

# H3 configuration
h3.cmd("ip route add default via 192.168.2.1")
h3.cmd("arp -s 192.168.2.1 00:00:00:00:02:02")
h3.cmd("arp -s 192.168.2.14 00:00:00:00:00:04")

# H4 configuration
h4.cmd("ip route add default via 192.168.2.1")
h4.cmd("arp -s 192.168.2.1 00:00:00:00:02:02")
h4.cmd("arp -s 192.168.2.13 00:00:00:00:00:03")

# Initialize CLI
CLI( net )

# Stop mininet network
net.stop()