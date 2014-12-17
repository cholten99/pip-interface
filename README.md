# Web-to-windows

### Requires:
1. mongoDB installed and running
 1. mongoDB driver for python ("pip install pika")
 2. mongoDB driver for PHP (http://php.net/manual/en/mongo.installation.php#mongo.installation.nix)
2. RabbitMQ installed and running
 1. RabbitMQ driver for python ("pip install pymongo")
 2. RabbitMQ driver for PHP (for php-amqplib see http://www.rabbitmq.com/tutorials/tutorial-one-php.html)
3. The Automa library (http://www.getautoma.com/docs/python_integration) -- remember to update the PYTHONPATH!

**Beware! If you CTRL+Z rather than CTRL+C a RabbitMQ consuming process it continues to run in the background!**
