# Python bazaviy imij
FROM python:3.11-slim

# Ishchi katalogni yaratish
WORKDIR /app

# requirements.txt va main.py fayllarini konteynerga nusxalash
COPY requirements.txt .
COPY main.py .

# Talab qilinadigan kutubxonalarni o‘rnatish
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8001

# Ilovani ishga tushirish
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
