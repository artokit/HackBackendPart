FROM python:3.11.9-slim-bullseye

RUN mkdir /workspace && mkdir  /workspace/project

WORKDIR /workspace/project

COPY backend/requirements.txt /workspace/project

COPY certs /workspace/certs
COPY .env /workspace

RUN pip install --upgrade -r requirements.txt

WORKDIR /workspace/project/src
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]