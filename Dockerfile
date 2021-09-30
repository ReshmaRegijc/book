FROM python:3.8-alpine
WORKDIR /book/app
COPY app.py /book/app/
COPY ./book/__init__.py /book/app/__init__.py 
COPY ./book/templates/ /book/app/templates
COPY requirements.txt /book/app/

RUN pip install -r requirements.txt

CMD ["python","app.py"]