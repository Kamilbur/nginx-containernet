# nginx-containernet

### Installation and run

* Install containernet (https://github.com/containernet/containernet) - it was tested on ubuntu 20.04 using containernet branch [ubuntu\_2004](https://github.com/containernet/containernet/tree/ubuntu_2004). Installation should not be in container, because nested containers don't respect memory and cpu limits. Virtual machine is recommended.
* Switch to appropriate branch [plus|open].
* Build docker images in docker directory
  ```bash
  $ cd docker
  $ sudo bash build.sh [base]
  ```
  where [base] indicate nginx version - plus for nginx plus or open for open source nginx. For more info just run build.sh without arguments (nginx plus build needs a nginx key).
* Go to src and run `main.py` file.
  ```bash
  cd src
  sudo python3 main.py
  ```
  It will run programmed benchmarks.
