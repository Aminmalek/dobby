from kafka import KafkaConsumer
import json

class KafkaConsumerWrapper:
    def __init__(self, broker, topic):
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=broker,
            value_deserializer=lambda v: json.loads(v.decode("utf-8")),
            api_version=(3, 9, 0),
        )
        self.consumer.subscribe([topic])
        self.topic = topic

    def consume(self):
        print(".........start consume........")
        for message in self.consumer:
            try:
                print(f"Received message: {message.value}")
                yield message.value
            except Exception as e:
                print(f"Error processing message: {e}")