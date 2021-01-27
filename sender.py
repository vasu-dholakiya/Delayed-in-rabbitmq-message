import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

message = "Message after 05  seconds"

# Declared exchange with Direct type
channel.exchange_declare("test-x", exchange_type="x-delayed-message", arguments={"x-delayed-type": "direct"})

# Publish message with delay of 5 seconds with x-delay property.
channel.basic_publish('test-x', 'delayed_message', message, properties=pika.BasicProperties(headers={"x-delay": 5000}))

print("message sent!!!")

connection.close()
