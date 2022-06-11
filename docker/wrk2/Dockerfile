FROM ubuntu:20.04


RUN apt-get update  && \
    apt-get install -y --no-install-recommends \
        git \
        make \
        gcc \
        curl \
        libghc-zlib-dev \
        net-tools \
        iproute2 \
        iputils-ping \
        libc6-dev \
        ca-certificates \
    && \
    rm -rf /var/lib/apt/lists/*


WORKDIR /tmp

RUN curl -L --output openssl.tar.gz https://ftp.openssl.org/source/old/1.1.1/openssl-1.1.1i.tar.gz  && \
    tar xzf openssl.tar.gz  && \
    cd openssl-1.1.1i  && \
    ./config  && \
    make  && \
    make install


RUN git clone https://github.com/giltene/wrk2.git  && \
    cd wrk2  && \
    make  && \
    mv wrk /usr/local/bin

WORKDIR /root


#  66  tar xzf openssl-1.1.1i.tar.gz 
#   67  ls
#   68  cd openssl-1.1.1i
#   69  ls
#   70  make 
#   71  ./config
#   72  ls
#   73  make
#   74  make install
#   75  cd /wrk2/
#   76  ls
#   77  make
#   78  apt-cache search zlib
#   79  sudo apt-get install zlibc
#   80  make
#   81  suod make
#   82  sudo make
#   83  cd deps/
#   84  ls
#   85  cd luajit/
#   86  ls
#   87  make
#   88  ls
#   89  cd src/
#   90  ls
#   91  cd ..
#   92  ls
#   93  cd ..
#   94  ls
#   95  cd ..
#   96  ls
#   97  apt-cache search zlib
#   98  sudo apt-get install libghc-zlib-dev
#   99  sudo make
#  100  make install
#  100  wrk
#  102  ls
#  103  wrk
#  104  ./wrk
#  105  echo $PATH
#  106  vi wrk 
#  107  mv wrk /usr/local/bin
#  108  wrk

CMD /bin/bash
