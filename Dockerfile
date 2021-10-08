FROM python:3.8.10

WORKDIR /book/app

COPY . .

RUN pip install --upgrade pip

RUN pip install email_validator

RUN pip install flask-dance

RUN pip3 install psycopg2

RUN pip install -r requirements.txt


CMD ["python","app.py"]