import sys
import pika

#durable flag for the case, if rabbit mq server dies messages should not be lost

#by default acknowledgement is on

#this is competing consumers pattern
#1 sender and multiple consumers to complete numerous tasks

queue_name = "task_queue"

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue=queue_name,durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
print("sending message -> ", message)

channel.basic_publish(exchange='',
                      routing_key=queue_name,
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))

print(" [x] Sent %r" % message)
