FROM python:3.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /apiFilmes
WORKDIR /apiFilmes
# Installing OS Dependencies
RUN pip install -U pip setuptools
COPY requirements.txt /apiFilmes/
RUN pip install -r /apiFilmes/requirements.txt
ADD . /apiFilmes/
# Django service
EXPOSE 8000

