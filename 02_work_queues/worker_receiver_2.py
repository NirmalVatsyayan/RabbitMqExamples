import time
import pika

queue_name = "task_queue"

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue=queue_name,durable=True)
#channel.basic_qos(prefetch_count=1)

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_consume(callback,
                      queue=queue_name)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
