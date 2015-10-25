FROM ubuntu:15.04

MAINTAINER "Tom Marks"

RUN ["apt-get", "install", "-y", "python-setuptools", "python-dev", "curl"]
#RUN ["apt-get", "install", "-y", "build-essential", "autoconf", "libtool"]
#RUN ["apt-get", "install", "-y", "libffi-dev", "libssl-dev"]
RUN curl https://bootstrap.pypa.io/get-pip.py | python

COPY ["./requirements.txt", "/tmp/requirements.txt"]
RUN ["pip", "install", "-r", "/tmp/requirements.txt"]

VOLUME ["/App"]

ENTRYPOINT ["python", "/App/run.py"]
CMD []
