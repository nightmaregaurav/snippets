<?php
  ###################################################
  ##        Author : Gaurav nyaupane               ##
  ###################################################
$date = (new DateTime())->setTimeZone(new DateTimeZone('Asia/Kathmandu'))->format('Y-m-d h:i:s A');//set time foramt
$host= gethostname();//find server hostmane
$hostip = gethostbyname($host);//find server host ip
  $file = fopen("Captured.txt","a");
  fwrite($file,"************************************************************************************************************************************************");
  fwrite($file,"\r\n");
  fwrite($file,"Date \t\t:-\t\t ");//print date
  fwrite($file,$date);
  fwrite($file,"\r\n");
  fwrite($file,"Host(webserver) \t\t:-\t\t ");//print hostname
  fwrite($file,$host);
  fwrite($file,"\r\n");
  fwrite($file,"Host ip \t\t:-\t\t ");//print host ip
  fwrite($file,$hostip);
  foreach($_SERVER as $variable=>$value){//loop for $_SERVER header
    fwrite($file,"\r\n");
    fwrite($file,$variable);
    fwrite($file," \t\t:-\t\t ");
    if(is_array($value)){
        foreach($value as $var=>$val){
            fwrite($file,"\r\n");
            fwrite($file,$var);
            fwrite($file," \t\t=>\t\t ");
            fwrite($file,$val);
        }        
    }
    else{
        fwrite($file,$value);
    }
  }
  foreach($_REQUEST as $variable=>$value){//loop for $_REQUEST header ($_REQUEST is $_GET, $_POST and $_COOKIE)
    fwrite($file,"\r\n");
    fwrite($file,$variable);
    fwrite($file," \t\t:-\t\t ");
    fwrite($file,$value);
  }
  $ip = substr($_SERVER['HTTP_HOST'],0,strpos($_SERVER['HTTP_HOST'],':'));
  if(strlen($ip)>0)
    fwrite($file,"IP of site: \t\t:-\t\t ".$value);
  fclose($file);
?>
