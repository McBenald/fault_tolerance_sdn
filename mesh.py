from mininet.topo import Topo  
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSSwitch
from mininet.topo import Topo


class VLANHost( Host ):
        def config( self, vlan=100, **params ):
                """Configure VLANHosts """
                r = super( Host, self ).config( **params )
                intf = self.defaultIntf()
                self.cmd( 'ifconfig %s inet 0' % intf )
                self.cmd( 'vconfig add %s %d' % ( intf, vlan ) )
                self.cmd( 'ifconfig %s.%d inet %s' % ( intf, vlan, params['ip'] ) )
                newName = '%s.%d' % ( intf, vlan )
                intf.name = newName
                self.nameToIntf[ newName ] = intf
                return r

class MyTopo( Topo ):  
    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts
        h1 = self.addHost( 'h1' , mac='10:10:10:02:20:01', ip='222.0.0.1/24', cls=VLANHost, vlan=400)
        h2 = self.addHost( 'h2' , mac='10:10:10:02:20:02', ip='222.0.0.2/24', cls=VLANHost, vlan=400)
        h3 = self.addHost( 'h3' , mac='10:10:10:02:20:03', ip='222.0.0.3/24', cls=VLANHost, vlan=400)
        h4 = self.addHost( 'h4' , mac='10:10:10:02:20:04', ip='222.0.0.4/24', cls=VLANHost, vlan=400)
        h5 = self.addHost( 'h5' , mac='10:10:10:02:20:05', ip='222.0.0.5/24', cls=VLANHost, vlan=400)
        h6 = self.addHost( 'h6' , mac='10:10:10:02:20:06', ip='222.0.0.6/24', cls=VLANHost, vlan=500)
        h7 = self.addHost( 'h7' , mac='10:10:10:02:20:07', ip='222.0.0.7/24', cls=VLANHost, vlan=500)
        SERVER = self.addHost( 'SERVER' , mac='02:00:00:00:20:03',ip='20.0.0.1/8')
        UDP = self.addHost( 'UDP' , mac='02:00:00:00:20:04',ip='40.0.0.1/8')

        # Add switches
        switches = []
        for i in range(4):
              name = 'switch' + str(i+1)
              switch = self.addSwitch(name, cls=OVSSwitch)
              switches.append(switch)

        #Connect hosts in a mesh
        for i in range(len(switches)):
                for j in range(i+1, len(switches)):
                        self.addLink(switches[i], switches[j])
        
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

