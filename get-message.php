<?php

# Weird includes for RabbitMQ
require_once __DIR__ . '/vendor/autoload.php';
use PhpAmqpLib\Connection\AMQPConnection;
use PhpAmqpLib\Message\AMQPMessage;

# Function to handle incomming message
$message_callback = function($message) {
  # Sed ACK to RabbitMQ
  $message->delivery_info['channel']->basic_ack($message->delivery_info['delivery_tag']);

  # Get data from mongoDB and send it
  $connection = new MongoClient();
  $collection = $connection->wtwinterface->wtwinterface;
  $data = $collection->findOne(array('_id' => new MongoId($message->body)));
  print json_encode($data) . "\n";
  $connection->close();
};

# MAIN
# Connect to RabbitMQ and wait for message
$connection = new AMQPConnection('localhost', 5672, 'guest', 'guest');
$channel = $connection->channel();

# Function to make sure we shut down properly
$shutdown_callback = function() {
  global $channel, $connection;
  $channel->close();
  $connection->close();
};
register_shutdown_function($shutdown_callback);

$channel->queue_declare('wtwinterface', false, false, false, false);
$channel->basic_qos(null, 1, null);
$channel->basic_consume('wtwinterface', '', false, false, false, false, $message_callback);
$channel->wait();

?>
