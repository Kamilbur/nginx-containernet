from mininet.log import info, setLogLevel

import topos.clitest as test
import topos.simple_lb as simple


setLogLevel('info')


def main():
    test.topo()
#    simple.topo()



if __name__ == '__main__':
    main()

