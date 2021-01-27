import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


# channel.queue_declare('FirstQueue')


def callback(ch, method, property, body):
    print(body)
    # print(property.headers)
    ch.basic_ack(delivery_tag=method.delivery_tag)


# Declared "first" queue.
channel.queue_declare(queue='first', durable=True)

# Bind the queue with exchange and route key
channel.queue_bind(queue="first", exchange="test-x", routing_key="delayed_message")

# Consuming From queue
channel.basic_consume(queue='first', auto_ack=False, on_message_callback=callback)

print("Consumer Waiting")
channel.start_consuming()
connection.close()
