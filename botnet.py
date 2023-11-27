from mininet.net import Mininet
from mininet.cli import CLI

def simulate_botnet(net, botnet_nodes, target_ip, duration):
    import time
    from subprocess import Popen

    # Starting attack from each botnet node
    attack_processes = []
    for node in botnet_nodes:
        host = net.getNodeByName(node)
        attack_process = host.popen(['ping', '-f', target_ip])
        attack_processes.append(attack_process)

    # Running the attack for the specified duration
    time.sleep(duration)

    # Stopping the attack
    for process in attack_processes:
        process.terminate()

if __name__ == '__main__':
    net = Mininet()  # Connect to an existing Mininet instance
    # CLI(net)  # This opens up the Mininet CLI

    botnet_node = 'h1'
    target_ip = '192.168.1.2'  # Replace with your web server's IP
    duration = 30  # Duration of the attack

    # Start the botnet simulation
    simulate_botnet(net, botnet_node, target_ip, duration)
