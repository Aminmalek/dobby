FROM python:3.10-slim
WORKDIR /app

COPY ./app /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt
#COPY create_topic.sh /app/create_topic.sh
#RUN chmod +x /app/create_topic.sh

# Ensure the script runs before your application starts
CMD ["python", "app.py"]
