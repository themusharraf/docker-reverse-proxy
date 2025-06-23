FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY main.py .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8002

CMD ["gunicorn", "main:app", "-b", "0.0.0.0:8002"]