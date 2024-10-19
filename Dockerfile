FROM python:3.10-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py makemigrations
RUN python manage.py migrate

FROM python:3.10-slim

COPY --from=builder /usr/local /usr/local

WORKDIR /app

COPY --from=builder /app /app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
