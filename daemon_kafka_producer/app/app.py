import time
from api_client import APIClient
from kafka_producer import KafkaProducerWrapper
from config import API_URL, KAFKA_BROKER, KAFKA_TOPIC

class App:
    def __init__(self):
        self.api_client = APIClient(API_URL)
        self.kafka_producer = KafkaProducerWrapper(KAFKA_BROKER, KAFKA_TOPIC)

    def run(self):
        while True:
            data = self.api_client.fetch_data()
            for record in data:
                self.kafka_producer.send_message(record)
            time.sleep(60)  # Run every minute

if __name__ == "__main__":
    print("Starting Kafka Producer Service...")
    service = App()
    service.run()
