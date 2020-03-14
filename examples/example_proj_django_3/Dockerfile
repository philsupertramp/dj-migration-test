FROM python:3
ENV PYTHONUNBUFFERED 1
ARG DJ_VERSION
RUN mkdir /code
COPY . /code
WORKDIR /code
RUN apt-get update
RUN apt-get upgrade -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install django==${DJ_VERSION:-3.0.4}
