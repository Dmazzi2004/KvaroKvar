FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
COPY app/ ./app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000
WORKDIR /app
CMD ["python", "app/main.py"]