FROM python:3.10-slim
WORKDIR /app

COPY ./app /app

COPY /../requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt
COPY create_topic.sh /usr/local/bin/create_topic.sh
RUN chmod +x /usr/local/bin/create_topic.sh

# Ensure the script runs before your application starts
CMD /usr/local/bin/wait-for-kafka.sh && python producer.py

