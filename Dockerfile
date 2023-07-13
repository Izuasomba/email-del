FROM python:3.9

WORKDIR /app

COPY . .

CMD ["python", "email_del.py"]

