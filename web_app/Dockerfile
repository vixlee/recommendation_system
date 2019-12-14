FROM python:3.7.0-alpine

EXPOSE 8000

COPY . /opt/web-app

WORKDIR /opt/web-app

COPY requirements.txt /opt/web-app/requirements.txt

RUN apk add --no-cache --virtual .build-deps postgresql-dev gcc musl-dev
RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt
COPY . .

CMD ["python3", "app.py"]