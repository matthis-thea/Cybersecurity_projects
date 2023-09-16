#coding:UTF-8
# Importing modules
from bs4 import BeautifulSoup as bs
import urllib.request
from PIL import Image
from pytesseract import pytesseract
import requests
import time
formulaire = requests.Session() # Allows to generate a session under the name of 'form' variables
 # ------------------------
 # Captcha breaking loop
for x in range(0, 10): # Added a for loop to maximize the chances of captcha breaking
    start = time.time()
    # Parse the Web Page and send a GET request to retrieve information about the page (below the cookies)
    url_challenge = "http://challenge01.root-me.org/programmation/ch8/"
    response = formulaire.get(url_challenge)
    soup = bs(response.text, features="lxml") # Will parse the page
    # ------------------------
   # Recovery of the captcha picture and creation of the file
    recuperation_link_image = soup.img['src']
    urllib.request.urlretrieve(recuperation_link_image,"orignal_captcha.png") 
    # Image processing
    picture_traitement = Image.open("orignal_captcha.png") 
    width, height = picture_traitement.size
    picture_copy = Image.new("L", picture_traitement.size) #L: grayscale mode
    couleur_fond = 255 # Equivalent to white color
    black = 0 # Equivalent to the color black
    # Copy of processing_image to copy_image
    for i in range(width):
        for j in range(height):
            r, g ,b = picture_traitement.getpixel((i,j)) # Take the color of pixel i,j in red and green and blue
            RGB = int((r + g + b)/3)
            if RGB == black or RGB == couleur_fond:
                picture_copy.putpixel((i, j), 255)
            else:
                picture_copy.putpixel((i, j), 0)
    picture_copy.save("modified_captcha.png")
    # Get the ASCII characters from the captcha in the copy_image
    path_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe" 
    picture_edit = Image.open("modified_captcha.png")
    pytesseract.tesseract_cmd = path_tesseract
    captcha = pytesseract.image_to_string(picture_edit)
    # Send for validation of the form
    captcha = captcha.split("\n")
    response_captcha = captcha[0]
    send_form = {"cametu" :response_captcha}
    response = formulaire.post(url=url_challenge, data=send_form, cookies=formulaire.cookies.get_dict())
    print(f"The HTML CODE {x}\n")
    print(response.text)
    end = time.time()
    difference = end - start
    print(f'Execution time : {difference:2}ms\n')
 # ------------------------
