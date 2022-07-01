FROM python:3.9-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY partner .
COPY core .
COPY manage.py .
CMD ["gunicorn", "--bind=0.0.0.0:8000", "core.wsgi"]