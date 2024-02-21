FROM python:3.8-slim

WORKDIR /app

RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0 && rm -rf /var/lib/apt/lists/*

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt


RUN pip install psycopg2-binary

EXPOSE 8000

CMD python create_table.py && uvicorn app:app --host 0.0.0.0 --port 8000
