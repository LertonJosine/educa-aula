FROM python:3.10-slim

WORKDIR /Educa

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

COPY /requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:8000 educa.wsgi:application && python manage.py migrate && python manage.py collectstatic"]