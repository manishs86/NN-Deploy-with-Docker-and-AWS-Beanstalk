FROM python:3.6-slim

WORKDIR /deploy/
COPY requirements.txt /deploy/

RUN apt-get update && \
      apt-get -y --no-install-recommends install sudo && \
      sudo apt-get -y --no-install-recommends install libsndfile1-dev && \
      pip install --no-cache-dir -r requirements.txt && \
      sudo rm -rf /var/lib/apt/lists/*

WORKDIR /deploy/
COPY . .

EXPOSE 5000

CMD ["python", "application.py"]
