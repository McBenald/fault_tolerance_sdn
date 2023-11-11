import pexpect

child = pexpect.spawn('onos localhost')

child.expect('onos>')

child.close()