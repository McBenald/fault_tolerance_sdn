import pexpect

def run_pingall():
    try:
        # Start ONOS CLI and execute 'pingall' command
        onos_cli = pexpect.spawn('onos localhost')
        onos_cli.expect('onos.*> ', timeout=60)  # Increased timeout to 60 seconds
        print("Connected to ONOS CLI")

        onos_cli.sendline('app activate org.onosproject.fwd')
        onos_cli.expect('onos.*> ', timeout=120)  # Increased timeout for pingall command
        print("fwd activated")

        onos_cli.sendline('app activate org.onosproject.openflow')
        onos_cli.expect('onos.*> ', timeout=120)  # Increased timeout for pingall command
        print("openflow activated")

        onos_cli.sendline('app activate org.onosproject.gui2')
        onos_cli.expect('onos.*> ', timeout=120)  # Increased timeout for pingall command
        print("gui2 activated")

        onos_cli.sendline('exit')  # Exit the ONOS CLI
        onos_cli.expect(pexpect.EOF)
        print("Exited ONOS CLI")
    except pexpect.ExceptionPexpect as e:
        print("Error:", e)

if __name__ == '__main__':
    run_pingall()