FROM python:3.6.8-slim as Base

RUN apt-get update \
  && apt-get install -y curl libomp-dev libgomp1

WORKDIR /home/hdb-house-price-prediction

COPY requirements.txt /home/hdb-house-price-prediction/requirements.txt
RUN pip install -r requirements.txt

COPY . /home/hdb-house-price-prediction

RUN chmod +x bin/start_server.sh

EXPOSE 8080

CMD ["/home/hdb-house-price-prediction/bin/start_server.sh"]

