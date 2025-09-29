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

def handle_message(channel, method, properties, body):
    try:
        print(f'Received: \r {channel}, \r {method}, \r {properties}, \r {body.decode()}')
    except Exception as e:
        print(f'An error accured {e}')
    else:
        channel.basic_ack(delivery_tag=method.delivery_tag)  # if not errors - confirm message for rebbit


def main():
    with BlockingConnection(connection_params) as conn:
        with conn.channel() as channel:  # create channel
            channel.queue_declare(queue='test_message')  # create queue if not

            channel.basic_consume(
                queue='test_message',
                on_message_callback=handle_message,  # handler
            )  # get from message
            print(' [x] Waiting message')
            channel.start_consuming()  # always waiting

if __name__ == '__main__':
    main()