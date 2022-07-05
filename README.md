# nginx-containernet

### Installation

* Install containernet (https://github.com/containernet/containernet) - it was tested on ubuntu 20.04 using containernet branch [ubuntu\_2004](https://github.com/containernet/containernet/tree/ubuntu_2004). Installation should be on bare-metal, because nested containers don't respect limits.
* Build docker images in docker directory
  ```bash
  $ cd docker
  $ sudo bash build.sh [base]
  ```
  where [base] indicate nginx version.
* Run `main.py` file. (Adjust topology)
