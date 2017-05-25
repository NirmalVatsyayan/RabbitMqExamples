'''
Exchange types could be :
    direct, topic, headers and fanout.

fanout just broadcasts a message to all queues.
direct exchange is used in routing of messages to any
particular key.
'''

#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#declare an exchange
channel.exchange_declare(exchange='logs',
                         type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"


channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print(" [x] Sent %r" % message)

connection.close()

