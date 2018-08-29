FROM ubuntu:latest
MAINTAINER Fagani Hajizada "hacizade.faqani@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
ADD . /flask-app
WORKDIR /flask-app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["flask-docker.py"]
ENV MESSAGE "IBO IBO IBO"
