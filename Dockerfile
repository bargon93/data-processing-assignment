FROM python:3.10-slim

WORKDIR /app

COPY reqs.txt .
RUN pip install --no-cache-dir -r reqs.txt

COPY *.py .

CMD ["python", "main.py"]