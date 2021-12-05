FROM python:3.8

WORKDIR /home/qanary_example

COPY requirements.txt ./
RUN pip install --upgrade pip -r requirements.txt; exit 0
RUN pip install gunicorn

COPY bert_qa_component.py  ./