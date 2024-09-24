FROM python:3.10-slim

WORKDIR /app

RUN pip install --no-cache-dir pandas openpyxl

COPY *.py .

CMD ["python", "main.py"]