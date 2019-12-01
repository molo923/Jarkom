from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink
import os

def protopo() :

	#clear mininet connection
	os.system('mn -c')
	net = Mininet(link=TCLink)

	#add host and router
	h1 = net.addHost('h1',ip='192.168.1.2/24', defaultRoute='via 192.168.1.1')
	h2 = net.addHost('h2',ip='192.168.2.2/24', defaultRoute='via 192.168.2.1')
	r1 = net.addHost('r1', ip='192.168.1.1/24')

	#connect 
	net.addLink(h1,r1, intfName='r1-eth0', params2={'ip' : '192.168.1.1/24'},bw=2,max_queue_size=80)
	net.addLink(h2,r1, intfName='r1-eth1', params2={'ip' : '192.168.2.1/24'},bw=1000,max_queue_size=80)

        #build the topo that have been given
        net.build()
        r1.cmd("ifconfig r1-eth0 0")
        r1.cmd("ifconfig r1-eth1 0")
        r1.cmd("ip addr add 192.168.1.1/24 brd + dev r1-eth0")
        r1.cmd("ip addr add 192.168.2.1/24 brd + dev r1-eth1")
        r1.cmd("sysctl -w net.ipv4.ip_forward=1")
        h1.cmd("ip route add default via 192.168.1.1")
        h2.cmd("ip route add default via 192.168.2.1")


	#congestion control
	h1.cmd("sysctl -w net.ipv4.tcp_congestion_control=reno")
	h2.cmd("sysctl -w net.ipv4.tcp_congestion_control=reno")

	net.start()
        info("\n\n",net.ping(),"\n")

	
	#start mininet
	CLI(net)
	
	#stop mininet
	net.stop()

if __name__ == '__main__':
	setLogLevel('info')
	protopo()
