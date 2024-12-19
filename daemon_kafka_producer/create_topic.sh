#!/bin/bash
# Wait for Kafka to be ready
until docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --list; do
  echo "Waiting for Kafka to be ready..."
  sleep 3
done
echo "Kafka is ready!"
