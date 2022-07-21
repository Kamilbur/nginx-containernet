from mininet.node import Controller
from mininet.link import TCLink
from mininet.log import info, setLogLevel

from utils.net import containernet_handler




def topo(topofilename='topo.out', measfilename='meas.out', **kwargs):

    with containernet_handler(controller=Controller) as net:

        info('*** Adding controller\n')
    
        net.addController('c0')
    
        info('*** Adding docker containers\n')


        srv_limits = {
            'cpu_quota':        -1,
            'cpu_period':       None,
            'cpu_shares':       None,
            'mem_limit':        None,
            'memswap_limit':    None,
        }
        srv_limits = kwargs.get('limits') or srv_limits
        


        nginx = net.addDocker('nginx',
                            ip='10.0.0.251',
                            dimage="nginx-open-srv:latest",
                            ports=[80],
                            environment={
                                'SRV_PORT': '5000',
                                'LISTEN_PORT': '80',
                            },
                            **srv_limits
                            )

        wrk = net.addDocker('wrk',
                            ip='10.0.0.252',
                            dimage="wrk2:latest")
           
    
        info('*** Adding switches\n')
        
        s1 = net.addSwitch('s1')
        s2 = net.addSwitch('s2')
        s3 = net.addSwitch('s3')
    
        info('*** Creating links\n')
        
        net.addLink(wrk, s1)
        net.addLink(s1, s2, cls=TCLink, delay='100ms', bw=1)
        net.addLink(s2, nginx)
        
        info('*** Starting network\n')
        
        net.start()
        
    
        info('*** Setuping layer 4\n')
   
        nginx.cmd("envsubst < /root/nginx-conf/open.conf > /root/nginx-conf/default.conf && nginx -c /root/nginx-conf/default.conf")
        nginx.cmd("FLASK_APP=/root/matrix-srv/main.py flask run &")
    
        info('*** Running tests\n')

        commands = [
            'wrk -t2 -c100 -d30s -R2000 --latency http://10.0.0.251:80/mmul/10',
        ]
        commands = kwargs.get('commands') or commands


        results = []

        for comm in commands:
            print(f'Running: {comm}')
            results.append(wrk.cmd(comm))


        info('*** Saving results\n')

        
        with open(measfilename, 'w+') as f:
            f.write(str(srv_limits))
            f.write('\n')
            f.write('\n')
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



def webserver_test():
    commands = [
        'wrk -t2 -c100 -d30s -R2000 --latency http://10.0.0.251:80/mmul/10',
        'wrk -t2 -c100 -d30s -R2000 --latency http://10.0.0.251:80/mmul/20',
        'wrk -t2 -c100 -d30s -R2000 --latency http://10.0.0.251:80/mmul/30',
        'wrk -t2 -c100 -d30s -R2000 --latency http://10.0.0.251:80/lu/10',
        'wrk -t2 -c100 -d30s -R2000 --latency http://10.0.0.251:80/lu/20',
        'wrk -t2 -c100 -d30s -R2000 --latency http://10.0.0.251:80/lu/30',
        'wrk -t2 -c100 -d30s -R2000 --latency http://10.0.0.251:80/qr/10',
        'wrk -t2 -c100 -d30s -R2000 --latency http://10.0.0.251:80/qr/20',
        'wrk -t2 -c100 -d30s -R2000 --latency http://10.0.0.251:80/qr/30',
    ]

    cpu_period = 100000
    limits = {
        'cpu_quotas': int( 1.0 * cpu_period ),
        'cpu_period': cpu_period,
        'cpu_shares': None,
        'mem_limit': None,
        'memswap_limit': None,
    }

    # No limits
    single_webserver.topo(
        topofilename='results/topo-full.out',
        measfilename='results/meas-full.out',
        commands=commands,
        limits=limits
    )


    limits = {
        'cpu_quotas': int( 0.5 * cpu_period ),
        'cpu_period': cpu_period,
        'cpu_shares': None,
        'mem_limit': None,
        'memswap_limit': None,
    }

    # Half of cpu
    single_webserver.topo(
        topofilename='results/topo-half.out',
        measfilename='results/meas-half.out',
        commands=commands,
        limits=limits
    )


    limits = {
        'cpu_quotas': int( 0.25 * cpu_period ),
        'cpu_period': cpu_period,
        'cpu_shares': None,
        'mem_limit': None,
        'memswap_limit': None,
    }

    # Quater of cpu
    single_webserver.topo(
        topofilename='results/topo-quarter.out',
        measfilename='results/meas-quarter.out',
        commands=commands,
        limits=limits
    )


    limits = {
        'cpu_quotas': int( 0.25 * cpu_period ),
        'cpu_period': cpu_period,
        'cpu_shares': None,
        'mem_limit': '32m',
        'memswap_limit': -1,
    }

    # Memory 12m
    single_webserver.topo(
        topofilename='results/topo-quarter-mem32.out',
        measfilename='results/meas-quarter-mem32.out',
        commands=commands,
        limits=limits
    )


    limits = {
        'cpu_quotas': int( 0.25 * cpu_period ),
        'cpu_period': cpu_period,
        'cpu_shares': None,
        'mem_limit': '16m',
        'memswap_limit': -1,
    }

    # Memory 6m
    single_webserver.topo(
        topofilename='results/topo-quarter-mem16.out',
        measfilename='results/meas-quarter-mem16.out',
        commands=commands,
        limits=limits
    )

