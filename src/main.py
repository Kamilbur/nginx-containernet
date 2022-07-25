from mininet.log import info, setLogLevel

import topos.clitest as test
import topos.simple_lb as simple
import topos.single_webserver as single_webserver
import topos.cluster as cluster

import os

setLogLevel('info')



def cluster_meas():
    commands = [
        'wrk -t2 -c100 -d30s -R2000 --latency http://10.0.0.25:80/mmul/15',
        'wrk -t2 -c100 -d30s -R2000 --latency http://10.0.0.25:80/lu/15',
        'wrk -t2 -c100 -d30s -R2000 --latency http://10.0.0.25:80/qr/15',
    ]

    if not os.path.isdir('results'):
        os.mkdir('results')

    # Cluster

    cpu_period = 100000
    limits = {
        'cpu_quotas': int( 1.0 * cpu_period ),
        'cpu_period': cpu_period,
        'cpu_shares': None,
        'mem_limit': '1024m',
        'memswap_limit': None,
    }
    cluster.topo(
        topofilename='results/topo.out',
        measfilename='results/klast-meas-1.out',
        weights=[1,1],
        commands=commands,
        limits=limits
        )


    limits = {
        'cpu_quotas': int( 2.0 * cpu_period ),
        'cpu_period': cpu_period,
        'cpu_shares': None,
        'mem_limit': '1024m',
        'memswap_limit': None,
    }
    cluster.topo(
        measfilename='results/klast-meas-2.out',
        weights=[1,1],
        commands=commands,
        limits=limits
        )


    limits = {
        'cpu_quotas': int( 3.0 * cpu_period ),
        'cpu_period': cpu_period,
        'cpu_shares': None,
        'mem_limit': '1024m',
        'memswap_limit': None,
    }
    cluster.topo(
        measfilename='results/klast-meas-3.out',
        weights=[1,1],
        commands=commands,
        limits=limits
        )


    # Single

    limits = {
        'cpu_quotas': int( 1.0 * cpu_period ),
        'cpu_period': cpu_period,
        'cpu_shares': None,
        'mem_limit': '1024m',
        'memswap_limit': None,
    }
    cluster.topo(
        measfilename='results/singl-meas-1.out',
        weights=[1,0],
        commands=commands,
        limits=limits
        )


    limits = {
        'cpu_quotas': int( 2.0 * cpu_period ),
        'cpu_period': cpu_period,
        'cpu_shares': None,
        'mem_limit': '1024m',
        'memswap_limit': None,
    }
    cluster.topo(
        measfilename='results/singl-meas-2.out',
        weights=[1,0],
        commands=commands,
        limits=limits
        )


    limits = {
        'cpu_quotas': int( 3.0 * cpu_period ),
        'cpu_period': cpu_period,
        'cpu_shares': None,
        'mem_limit': '1024m',
        'memswap_limit': None,
    }
    cluster.topo(
        measfilename='results/singl-meas-3.out',
        weights=[1,0],
        commands=commands,
        limits=limits
        )



def main():
#    test.topo()
#    simple.topo()
#    single_webserver.webserver_test()
    cluster_meas()


if __name__ == '__main__':
    main()

