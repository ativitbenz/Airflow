FROM apache/airflow:2.3.0
USER root
# # for upgrade version python ##
# FROM python:3.9
# RUN python -m pip install \
#         parse \
#         realpython-reader

# install library for fixed issues library apache provider not found 
RUN apt-get update && apt-get install gcc g++ libsasl2-dev -y 
RUN curl -sSL https://get.docker.com/ | sh
USER airflow
COPY requirements.txt /requirements.txt
RUN pip install --user --upgrade pip
RUN pip install --no-cache-dir --user -r /requirements.txt
RUN export AIRFLOW__SMTP__SMTP_HOST AIRFLOW__SMTP__SMTP_PORT AIRFLOW__SMTP__SMTP_USER AIRFLOW__SMTP__SMTP_PASSWORD AIRFLOW__SMTP__SMTP_MAIL_FROM

### step run for install package dependencies
# docker build . --tag extending_airflow:latest -> for update pip installation
# docker-compose up -d --no-deps --build airflow-webserver airflow-scheduler -> for reset connect docker contenerd
# docker-compose -f docker-compose-test.yaml up -d --no-deps --build airflow-webserver airflow-scheduler
