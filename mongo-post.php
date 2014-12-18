<?php

$uid = $_POST["uid"];

$connection = new MongoClient();
$collection = $connection->wtwinterface->wtwinterface;

$newdata = array('$set' => array("ProcStatus" => "Processed"));
$collection->update(array("_id" => new MongoId($uid)), $newdata);

?>
