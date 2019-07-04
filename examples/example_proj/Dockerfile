FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
COPY . /code
WORKDIR /code
RUN apt-get update
RUN apt-get upgrade -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install django==$DJ_VERSION
