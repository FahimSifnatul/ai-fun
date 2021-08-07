FROM python:3.8-slim-buster
WORKDIR /puthon_funplay
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN python manage.py collectstatic
COPY . .
