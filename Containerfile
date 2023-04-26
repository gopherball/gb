FROM registry.fedoraproject.org/fedora-minimal:latest

RUN dnf5 -y upgrade
RUN dnf5 -y install python3 python3-pip

RUN mkdir /data
RUN mkdir /app

WORKDIR /app

RUN python -m venv venv
RUN venv/bin/pip install -U pip
RUN venv/bin/pip install gb

EXPOSE 7070

CMD ["/app/venv/bin/gb", "-m", "implicit", "--magic", "/data"]
