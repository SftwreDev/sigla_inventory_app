FROM python:3.9.6
ENV PYTHONUNBUFFERED=1
EXPOSE 8080
WORKDIR /
COPY requirements.txt /
RUN pip install -r requirements.txt
COPY . /
