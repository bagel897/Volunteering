FROM python:3
ENV PYTHONUNBUFFERED 1
RUN apk update && \
     apk add --virtual build-deps gcc python-dev musl-dev && \
     apk add postgresql-dev bash
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN python manage.py makemigrations
RUN python manage.py migrate
ENV DOCKERTRUE Yes
