FROM python:3.8-slim-buster
WORKDIR /python_funplay
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
