FROM rasa/rasa:3.6.21

WORKDIR /app

COPY . /app

USER root

RUN pip install flask requests

EXPOSE 5005

CMD ["run", "--enable-api", "--cors", "*", "--host", "0.0.0.0", "--port", "5005"]