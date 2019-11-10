FROM centos:7

RUN yum update -y && \
    yum clean all && \
    rm -rf /var/cache/yum && \
    rpm -ivh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm && \
    yum install -y gcc gcc-c++ python2-devel python2-pip sudo && \
    pip install -U pip setuptools && \
    pip install --ignore-installed -U ipaddress && \
    pip install rally rally-openstack python-openstackclient elasticsearch \
     elasticsearch configparser statistics numpy scipy redis

RUN useradd -ms /bin/bash stack && \
    echo "stack ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

RUN mkdir -p /etc/rally /var/lib/rally/data && \
    chown -R stack:stack /var/lib/rally/data && \
    echo "[database]" > /etc/rally/rally.conf && \
    echo "connection=sqlite://///var/lib/rally/data/rally.db" >> /etc/rally/rally.conf

VOLUME  ["/var/lib/rally/data"]

RUN mkdir -pv /opt/snafu
COPY . /opt/snafu/

RUN rally db recreate
USER stack
