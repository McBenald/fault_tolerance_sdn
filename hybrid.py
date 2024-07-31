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
        h11 = self.addHost( 'h11' , mac='10:10:10:02:20:01', ip='222.0.0.1/24')
        h12 = self.addHost( 'h12' , mac='10:10:10:02:20:02', ip='222.0.0.2/24')
        h13 = self.addHost( 'h13' , mac='10:10:10:02:20:03', ip='222.0.0.3/24')
        h14 = self.addHost( 'h14' , mac='10:10:10:02:20:04', ip='222.0.0.4/24')
        h15 = self.addHost( 'h15' , mac='10:10:10:02:20:05', ip='222.0.0.5/24')
        h16 = self.addHost( 'h16' , mac='10:10:10:02:20:06', ip='222.0.0.6/24')
        h17 = self.addHost( 'h17' , mac='10:10:10:02:20:07', ip='222.0.0.7/24')
        SERVER = self.addHost( 'SERVER' , mac='02:00:00:00:20:03',ip='20.0.0.1/8')
        UDP = self.addHost( 'UDP' , mac='02:00:00:00:20:04',ip='40.0.0.1/8')

        # Add switches
        switches = []
        for i in range(10, 14):
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

        self.addLink( h11, switches[0] )
        self.addLink( h12, switches[2] )
        self.addLink( h13, switches[0] )
        self.addLink( SERVER, switches[0] )
        self.addLink( h14, switches[3] )
        self.addLink( h15, switches[3] )
        self.addLink( h16, switches[1] )
        self.addLink( h17, switches[1] )
        self.addLink( UDP, switches[2] )


	
        
topos = { 'mytopo': ( lambda: MyTopo() ) } 
