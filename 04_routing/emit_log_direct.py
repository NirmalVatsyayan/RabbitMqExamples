#!/usr/bin/env python
import pika
import sys

#python emit_log_direct.py error "Run. Run. Or it will explode."

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         type='direct')

severity = sys.argv[1] if len(sys.argv) > 2 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)

print(" [x] Sent %r:%r" % (severity, message))
connection.close()