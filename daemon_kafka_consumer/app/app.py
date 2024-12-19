from time import sleep

from kafka_consumer import KafkaConsumerWrapper
from elastic_client import ElasticClient
from config import KAFKA_BROKER, KAFKA_TOPIC, ELASTIC_HOST, ELASTIC_INDEX


class App:
    def __init__(self):
        self.elastic_client = ElasticClient(ELASTIC_HOST, ELASTIC_INDEX)
        self.kafka_consumer = KafkaConsumerWrapper(KAFKA_BROKER, KAFKA_TOPIC)

    def run(self):
        print(".............run..............")
        for message in self.kafka_consumer.consume():
            self.elastic_client.index_document(message)


if __name__ == "__main__":
    print("...Starting Kafka Consumer Service...")
    # This sleep time is for elastic to prepare and to prevent any connection issues
    sleep(30)
    service = App()
    service.run()