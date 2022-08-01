# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .

ENV DB_USER=root
ENV DB_PWD=root
ENV DB_HOST=mysql
ENV DB_NAME=python_flask
ENV DB_PORT=3306

CMD ["flask", "run"]