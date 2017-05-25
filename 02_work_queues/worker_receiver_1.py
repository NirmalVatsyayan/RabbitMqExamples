import time
import pika

'''
prefetch count is useful in conditions where say you have 2 workers or more
and a worker is getting all long work but other worker is getting light one

prefetch count says rabbitmq to not send messages to a worker till it is not
finished doing his work

assume you got 4 messages
say worker 1 takes 5 second but worker 2 took 1 second to finish a work
the third message will be given to worker 2 instead of worker 1 because
it is free.

In traditional round robin it will be given to worker 1

'''

queue_name = "task_queue"

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue=queue_name,durable=True)
#channel.basic_qos(prefetch_count=1)

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    time.sleep(2)
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_consume(callback,
                      queue=queue_name)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
