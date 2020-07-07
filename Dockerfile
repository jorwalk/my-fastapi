# https://pythonspeed.com/articles/base-image-python-docker-images/
FROM python:3.8-slim-buster
COPY requirements.txt /tmp
WORKDIR /tmp
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 8080
WORKDIR /

CMD ["uvicorn", "main:app", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8080"]    
