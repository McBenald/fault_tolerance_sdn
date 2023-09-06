from mininet.topo import Topo  
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSSwitch
from mininet.topo import Topo


class MyTopo( Topo ):  
    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts
        h1 = self.addHost( 'h1' , mac='10:10:10:02:20:01', ip='222.0.0.1/24')
        h2 = self.addHost( 'h2' , mac='10:10:10:02:20:02', ip='222.0.0.2/24')
        h3 = self.addHost( 'h3' , mac='10:10:10:02:20:03', ip='222.0.0.3/24')
        h4 = self.addHost( 'h4' , mac='10:10:10:02:20:04', ip='222.0.0.4/24')
        h5 = self.addHost( 'h5' , mac='10:10:10:02:20:05', ip='222.0.0.5/24')
        h6 = self.addHost( 'h6' , mac='10:10:10:02:20:06', ip='222.0.0.6/24')
        h7 = self.addHost( 'h7' , mac='10:10:10:02:20:07', ip='222.0.0.7/24')
        SERVER = self.addHost( 'SERVER' , mac='02:00:00:00:20:03',ip='20.0.0.1/8')
        UDP = self.addHost( 'UDP' , mac='02:00:00:00:20:04',ip='40.0.0.1/8')

        # Add switches
        switches = []
        for i in range(4):
              name = 'switch' + str(i+1)
              switch = self.addSwitch(name, cls=OVSSwitch)
              switches.append(switch)
        root_switch = self.addSwitch('switch0', cls=OVSSwitch, dpid='0000000000000010')

        #Connect hosts in a star
        for i in range(len(switches)):
              self.addLink(root_switch, switches[i])

        #connect switch in ring topology
        for i in range(len(switches)-1):
              self.addLink(switches[i], switches[i+1])
        self.addLink(switches[i+1], switches[0])
        
        # Add links 

        self.addLink( h1, switches[0] )
        self.addLink( h2, switches[2] )
        self.addLink( h3, switches[0] )
        self.addLink( SERVER, switches[0] )
        self.addLink( h4, switches[3] )
        self.addLink( h5, switches[3] )
        self.addLink( h6, switches[1] )
        self.addLink( h7, switches[1] )
        self.addLink( UDP, switches[2] )
	
	
        
topos = { 'mytopo': ( lambda: MyTopo() ) } 