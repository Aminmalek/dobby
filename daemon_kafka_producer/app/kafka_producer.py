from kafka import KafkaProducer
import json

class KafkaProducerWrapper:
    def __init__(self, broker, topic):
        self.producer = KafkaProducer(
            bootstrap_servers=broker,
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
            api_version=(3, 9, 0),
        )
        self.topic = topic

    def send_message(self, message):
        self.producer.send(self.topic, message)
        self.producer.flush()



