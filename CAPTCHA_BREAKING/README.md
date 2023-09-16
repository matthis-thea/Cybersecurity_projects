# Captcha_breaking
This code is for a CTF. It's a code for break a captcha with 30 or 40 percent of success. At the start, the captcha was like this :

<img width="217" alt="Screen Shot 2023-01-28 at 7 34 38 PM" src="https://github.com/matthis-thea/Captcha_breaking/blob/main/orignal_captcha.png">

Once the captcha has been captured,, we will obfuscate the captcha like this : 

<img width="217" alt="Screen Shot 2023-01-28 at 7 34 38 PM" src="https://github.com/matthis-thea/Captcha_breaking/blob/main/modified_captcha.png">

Once we have that, we will use Tesseract which is a character recognition tool and will allow us to capture the characters and put them into an array.
Tesseract is not optimal, which is why the success percentage is minimal.
