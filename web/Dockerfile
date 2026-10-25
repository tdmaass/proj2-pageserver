FROM python:2.7
MAINTAINER Trevor Maass "tmaass@uoregon.edu"
RUN sed -i 's/deb.debian.org/archive.debian.org/g' /etc/apt/sources.list && \
    sed -i 's/security.debian.org/archive.debian.org/g' /etc/apt/sources.list && \
    # Disable expired security updates for oldstable to avoid 404s
    sed -i '/security.debian.org/d' /etc/apt/sources.list
RUN apt-get update -y
RUN apt-get install -y python-pip python3-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
