FROM python:3.9-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY partner ./partner
COPY core ./core
COPY manage.py .
COPY wait_for .