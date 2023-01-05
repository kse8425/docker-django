FROM python:3.8.10-slim

ADD . /app

WORKDIR /app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

CMD ["python","manage.py","runserver","0.0.0.0:8000"]

EXPOSE 8000