FROM python:3.8-slim-buster
# ENV DJANGO_SECRET_KEY
RUN mkdir /app
# Installing OS Dependencies
WORKDIR /app
COPY . ./
EXPOSE 8000
RUN chmod +x run_web.sh && ./run_web.sh
ENTRYPOINT python3 manage.py runserver 0.0.0.0:8000
