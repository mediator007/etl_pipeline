FROM python:3.11-slim

RUN apt-get update && apt-get install -y nginx

RUN mkdir -p /home/ubuntu/sites/university-domains-list-api/logs

COPY ./university-domains-list-api/conf/nginx.conf /etc/nginx/sites-available/default

WORKDIR /app

COPY ./university-domains-list-api/requirements.txt ./
RUN pip install -r requirements.txt

COPY ./university-domains-list-api .

EXPOSE 80

CMD service nginx start && python app.py

