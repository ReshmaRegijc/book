FROM python:3.8.10
WORKDIR /book/app

COPY . .

RUN pip install -r requirements.txt

CMD ["python","app.py"]