FROM python:3.10-slim-buster

WORKDIR /python-docker


COPY . .

ENV FLASK_APP=main.py

RUN pip3 install -r requirements.txt

CMD [ "flask", "run", "--host=0.0.0.0", "--port=8080"]
