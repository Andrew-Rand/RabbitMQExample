import os

from dotenv import load_dotenv
from pika import ConnectionParameters, BlockingConnection, PlainCredentials

load_dotenv()


connection_params = ConnectionParameters(
    host='localhost',
    port=5672,
    credentials=PlainCredentials(
        username=os.getenv('RABBITMQ_DEFAULT_USER'),
        password=os.getenv('RABBITMQ_DEFAULT_PASS'),
    )
)


def main():
    with BlockingConnection(connection_params) as conn:
        with conn.channel() as channel:  # create channel
            channel.queue_declare(queue='test_message')  # create queue if not

            channel.basic_publish(
                exchange="",  # use direct exchange
                routing_key='test_message',  # to queue "test_messages"
                body='Hello World!',
            )  # publish message
            print("Sent 'Hello World!'")

if __name__ == '__main__':
    main()