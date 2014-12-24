<?php

$commands = [];
$directory = "../scripts";
$files = array_diff(scandir($directory), array('..', '.'));
foreach($files as $file) {
  $commands[basename($file, ".json")] = json_decode(file_get_contents("../scripts/" . $file));
}
print json_encode($commands);


?>
