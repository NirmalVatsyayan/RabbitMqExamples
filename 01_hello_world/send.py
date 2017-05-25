import pika

queue_name = "hello_queue"

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue=queue_name)

channel.basic_publish(exchange='',
                      routing_key=queue_name,
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()
