from mininet.log import info, setLogLevel

import topos.clitest as test
import topos.simple_lb as simple
import topos.single_webserver as single_webserver
import topos.cluster as cluster

setLogLevel('info')


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
    



def main():
#    test.topo()
#    simple.topo()
#    webserver_test()
    cluster.topo()
    



if __name__ == '__main__':
    main()

