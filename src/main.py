from mininet.node import Controller
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import info, setLogLevel

from utils import containernet


#, dcmd="/docker-entrypoint.sh /bin/sh -c /bin/bash"), environment={"NGINX_PORT": "80", "NGINX_HOST": "10.0.0.251"})

setLogLevel('info')

#net = Containernet(controller=Controller)

with containernet(controller=Controller) as net:

    info('*** Adding controller\n')

    net.addController('c0')

    info('*** Adding docker containers\n')

    nginx = net.addDocker('nginx', ip='10.0.0.251', dimage="nginxx:latest", ports=[80], port_bindings={80: 80})
    wrk = net.addDocker('wrk', ip='10.0.0.252', dimage="wrk2:latest")
    
    info('*** Adding switches\n')
    
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')

    info('*** Creating links\n')
    
    net.addLink(wrk, s1)
    net.addLink(s1, s2, cls=TCLink, delay='100ms', bw=1)
    net.addLink(s2, nginx)
    
    info('*** Starting network\n')
    
    net.start()
    

    info('*** Setuping layer 4\n')

    nginx.cmd("nginx")

    info('*** Testing connectivity\n')
    
    net.ping([wrk, nginx])
    info('*** Running CLI\n')
    
    CLI(net)


if __name__ == '__main__':
    pass

