FROM python:3

WORKDIR /code
COPY ./ ./

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "./src/manage.py", "runserver", "0.0.0.0:8000"]