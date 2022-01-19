<?php 
//$command= sprintf('python cambiarIp.py %s ', $_POST['estadoled']);

$comm= "python cambiarIp.py " .  $_POST["inputIP"] ." ".  $_POST["inputDIN"] ." ". $_POST["inputSSID"] ." ".  $_POST["inputPSWD"];
$command= sprintf($comm);
$resp = shell_exec($command);

echo $resp;
die();
?>