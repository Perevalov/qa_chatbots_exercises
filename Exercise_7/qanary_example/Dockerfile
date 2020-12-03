# Dockerfile for the Backend

FROM python:3.6.6-slim

WORKDIR /home/qanary_example

COPY requirements.txt ./

RUN pip install --upgrade pip -r requirements.txt; exit 0

COPY app app
COPY tests tests
COPY config.py run.py  ./

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD ["python", "run.py"]