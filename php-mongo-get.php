<?php

$uid = $_GET["uid"];

$connection = new MongoClient();
$collection = $connection->pipinterface->pipinterface;

$data = $collection->findOne(array('_id' => new MongoId($uid)));

print(json_encode($data));

?>
