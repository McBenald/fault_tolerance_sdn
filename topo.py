from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch
from mininet.link import TCLink
from mininet.nodelib import NAT
from mininet.log import info, setLogLevel
from mininet.node import Node, Host
from mininet.cli import CLI

class LinuxRouter(Node):
    def config(self, **params):
        super(LinuxRouter, self).config(**params)
        self.cmd('sysctl net.ipv4.ip_forward=1')

    def terminate(self):
        self.cmd('sysctl net.ipv4.ip_forward=0')
        super(LinuxRouter, self).terminate()


class CustomTopo(Topo):
    def build(self):
        #Add switch (Distribution Layer)
        s0 = self.addSwitch('s0', protocols='OpenFlow13', dpid='0000000000000010')

        #Add Switches (Access Layer)
        s1 = self.addSwitch('s1', protocols='OpenFlow13')
        s2 = self.addSwitch('s2', protocols='OpenFlow13')
        s3 = self.addSwitch('s3', protocols='OpenFlow13')

        #Add link for switches
        self.addLink(s1, s0)
        self.addLink(s2, s0)
        self.addLink(s3, s0)
        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s1, s3)
        
        # Add routers (Core Layer)
        r1 = self.addNode('r1', cls=LinuxRouter, ip='192.168.1.1/24')

        #link for router
        self.addLink(s0,
                     r1,
                     intfName2='r1-eth1',
                     params2={'ip': '192.168.1.1/24'})
        
        self.addLink(s0,
                     r1,
                     intfName2='r1-eth2',
                     params2={'ip': '192.168.2.1/24'})
        
        nat = self.addNode('nat', cls=NAT, ip='192.168.1.254', inNamespace=False)

        self.addLink(s0, nat)
        self.addLink(s1, nat)
        self.addLink(s2, nat)
        self.addLink(s3, nat)
        
        #Add Servers
        print_server = self.addHost('server1', ip='192.168.1.2/24', defaultRoute='via 192.168.1.1')
        dns_server = self.addHost('server2', ip='192.168.1.3/24', defaultRoute='via 192.168.1.1')

        #Add link for servers
        self.addLink(print_server, s1)
        self.addLink(dns_server, s1)

        #Add PCs
        h1 = self.addHost('h1', ip='192.168.1.11/24', mac='10:00:00:10:00:01', defaultRoute='via 192.168.1.1')
        h2 = self.addHost('h2', ip='192.168.1.12/24', mac='10:00:00:10:00:02', defaultRoute='via 192.168.1.1')
        h3 = self.addHost('h3', ip='192.168.1.13/24', mac='10:00:00:10:00:03', defaultRoute='via 192.168.1.1')
        h4 = self.addHost('h4', ip='192.168.1.14/24', mac='10:00:00:10:00:04', defaultRoute='via 192.168.1.1')
        h5 = self.addHost('h5', ip='192.168.1.15/24', mac='10:00:00:10:00:05', defaultRoute='via 192.168.1.1')
        h6 = self.addHost('h6', ip='192.168.1.16/24', mac='10:00:00:10:00:06', defaultRoute='via 192.168.1.1')
        h7 = self.addHost('h7', ip='192.168.1.17/24', mac='20:00:00:20:00:01', defaultRoute='via 192.168.1.1')
        h8 = self.addHost('h8', ip='192.168.1.18/24', mac='20:00:00:20:00:02', defaultRoute='via 192.168.1.1')


        #Add links for PCs
        self.addLink(h1, s2)
        self.addLink(h2, s3)
        self.addLink(h3, s2)
        self.addLink(h4, s3)
        self.addLink(h5, s2)
        self.addLink(h6, s3)
        self.addLink(h7, s2)
        self.addLink(h8, s3)

        
        

def network():
    topo= CustomTopo()

    net = Mininet(
        topo=topo,
        switch = OVSSwitch,
        link = TCLink,
        controller= RemoteController(name='remote', ip='127.0.0.1', port=6653, protocols='OpenFlow13')
    )
    
    
    net.start()

    server1 = net.get('server1')
    server1.cmd('route add default gw 192.168.1.254')
    
    h1 = net.get('h1')
    h1.cmd('route add default gw 192.168.1.254')
    h2 = net.get('h2')
    h2.cmd('route add default gw 192.168.1.254')
    h3 = net.get('h3')
    h3.cmd('route add default gw 192.168.1.254')
    h4 = net.get('h4')
    h4.cmd('route add default gw 192.168.1.254')
    h5 = net.get('h5')
    h5.cmd('route add default gw 192.168.1.254')
    h6 = net.get('h6')
    h6.cmd('route add default gw 192.168.1.254')
    h7 = net.get('h7')
    h7.cmd('route add default gw 192.168.1.254')
    h8 = net.get('h8')
    h8.cmd('route add default gw 192.168.1.254')

    # Install flask to host server
    server1.cmd('pip install flask')
    server1.cmd('python web_app.py &')
    
    
    # print routing table
    info( '*** Routing Table on Router:\n' )
    info( net[ 'r1' ].cmd( 'route' ) )



    #net.pingAll()



    CLI(net)

    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    network()
        
