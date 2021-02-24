FROM python:3.8

COPY . /code
WORKDIR /code
RUN pipenv install

CMD ["python3", "manage.py runserver"]