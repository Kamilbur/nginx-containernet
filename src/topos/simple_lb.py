from mininet.node import Controller
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import info, setLogLevel

from utils.net import containernet_handler




def topo(topofilename='topo.out', measfilename='meas.out', **kwargs):
    with containernet_handler(controller=Controller) as net:

        info('*** Adding controller\n')
    
        net.addController('c0')
    
        info('*** Adding docker containers\n')

        nginx = net.addDocker('nginx',
                            ip='10.0.0.251',
                            dimage="nginxx:latest",
                            ports=[80])
        wrk = net.addDocker('wrk',
                            ip='10.0.0.252',
                            dimage="wrk2:latest")
           
        servers_kwargs = {
            'srv1': {
                'ip': '10.0.0.10',
                'dimage': 'flask:latest',
                'ports': [5000],
                'environment': {'SRVNAME': 'srv1'}
                },
            'srv2': {
                'ip': '10.0.0.11',
                'dimage': 'flask:latest',
                'ports': [5000],
                'environment': {'SRVNAME': 'srv2'}
                },
            }
    
        servers = {}
    
    
        for key in servers_kwargs:
            servers[key] = net.addDocker(key, **servers_kwargs[key])
    
    
        info('*** Adding switches\n')
        
        s1 = net.addSwitch('s1')
        s2 = net.addSwitch('s2')
        s3 = net.addSwitch('s3')
    
        info('*** Creating links\n')
        
        net.addLink(wrk, s1)
        net.addLink(s1, s2, cls=TCLink, delay='100ms', bw=1)
        net.addLink(s2, nginx)
        net.addLink(s3, s2)
    
        for srv in servers.values():
            net.addLink(s3, srv)
        
        info('*** Starting network\n')
        
        net.start()
        
    
        info('*** Setuping layer 4\n')
    
        nginx.cmd("nginx -c /root/lb-config/simple_lb.conf")
    
        for srv in servers.values():
            srv.cmd("bash -c 'python3 -m flask run --host=0.0.0.0 2> /dev/null > /dev/null &'")
    
    
        info('*** Running tests\n')

        commands = [
            'wrk -t2 -c100 -d30s -R2000 --latency http://10.0.0.251:80',
        ]

        results = []

        for comm in commands:
            print(f'Running: {comm}')
            results.append(wrk.cmd(comm))


        info('*** Saving results\n')

        
        with open(measfilename, 'w+') as f:
            for i in range(len(commands)):
                f.write(commands[i])
                f.write('\n')
                f.write('\n')
                f.write(results[i])
                f.write('\n')


        with open(topofilename, 'w+') as f:
            for _, item in net.items():
                item_repr = repr(item)
                item_repr = item_repr.replace('<Docker ', '<Host ')
                f.write(item_repr)
                f.write('\n')

            f.write('\n')
            f.write('===' * 20)
            f.write('\n')
            
            for link in net.links:
                f.write(str(link))
                f.write('\n')

