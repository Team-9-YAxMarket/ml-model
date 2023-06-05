FROM python:3.10-slim

RUN python -m pip install --upgrade pip

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir

COPY run.py .
COPY src /app/src

EXPOSE 8080/tcp

CMD ["uvicorn", "run:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]

