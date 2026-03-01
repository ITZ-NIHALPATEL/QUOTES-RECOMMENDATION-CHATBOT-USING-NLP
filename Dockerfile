FROM rasa/rasa:3.6.21

WORKDIR /app

COPY . /app

USER root

RUN pip install flask requests

EXPOSE 5005

CMD rasa run --enable-api --cors "*" -i 0.0.0.0 -p $PORT