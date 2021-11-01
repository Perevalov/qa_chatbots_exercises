FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt; exit 0
RUN pip install uvicorn[standard]

COPY * ./

RUN chmod +x boot.sh
ENTRYPOINT ["./boot.sh"]