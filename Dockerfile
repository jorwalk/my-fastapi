# https://pythonspeed.com/articles/base-image-python-docker-images/
FROM python:3.8-slim-buster
COPY requirements.txt /tmp
WORKDIR /tmp
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
EXPOSE 8080
COPY ./ /app
WORKDIR /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]