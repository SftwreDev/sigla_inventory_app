FROM python:3.9
EXPOSE 8080
ENV PYTHONUNBUFFERED=1
WORKDIR /
COPY requirements.txt /
RUN pip install -r requirements.txt
COPY . /

CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]