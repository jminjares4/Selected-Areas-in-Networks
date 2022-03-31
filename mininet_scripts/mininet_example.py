from mininet.net import Mininet
from mininet.cli import CLI
from mininet.node import RemoteController


net = Mininet()

h1 = net.addHost(name='h1', mac='00:00:00:00:00:01',  ip='192.168.1.11', prefixLen=24)
h2 = net.addHost(name='h2', mac='00:00:00:00:00:02', ip='192.168.1.12', prefixLen=24)

s1 = net.addSwitch(name='s1')
ctrl = net.addController(name='c0', controller=RemoteController)
net.addLink(h1,s1)
net.addLink(h2,s1)

net.start()

CLI(net)

net.stop()