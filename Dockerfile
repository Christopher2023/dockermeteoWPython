FROM python:slim-buster

COPY . /app/

WORKDIR /app

RUN pip install --no-cache-dir requests==2.5.1

CMD [ "python", "meteo.py" ]