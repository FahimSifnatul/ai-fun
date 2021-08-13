FROM python:3.8-slim-buster
WORKDIR /python_funplay
COPY requirements.txt requirements.txt
RUN apt update
RUN pip install -r requirements.txt
COPY . .
CMD python manage.py collectstatic
