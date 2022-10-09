FROM python:3.9

EXPOSE 8080


RUN mkdir /app
COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python", "server.py"]