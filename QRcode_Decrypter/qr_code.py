from bs4 import BeautifulSoup as bs
from io import BytesIO
from PIL import Image
from PIL import ImageDraw
from pyzbar.pyzbar import decode
import requests
import base64
import urllib.request

formulaire = requests.Session()

url_challenge = "Put your URL here"
answer = formulaire.get(url_challenge)
soup = bs(answer.text, features="lxml")
recuperation_link_image = soup.img['src']
urllib.request.urlretrieve(recuperation_link_image,"original_QRcode.png") 
# split = recuperation_link_image.split(',') # I split this here because my picture was in base64 format like : data:image/png;base64,iVBODHJEFVEHFR==
recuperation_link_image = split[1]

image_decode = base64.b64decode(recuperation_link_image)
image = Image.open(BytesIO(image_decode))
draw = ImageDraw.Draw(image)

# Here it's to add the three square in the corners

# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# w = 9
# w2 = w * 2
# w5 = w * 5
# w6 = w * 6
# w7 = w * 7
# for x, y in [(18, 18), (18, 216), (216, 18)]:
#     draw.rectangle([(x, y), (x + w7, y + w7)], fill = BLACK)
#     draw.rectangle([(x + w, y + w), (x + w6, y + w6)], fill = WHITE)
#     draw.rectangle([(x + w2, y + w2), (x + w5, y + w5)], fill = BLACK)      
# image.save("modified_QRcode.png")

decodeQR = decode(Image.open('modified_QRcode.png'))
split = decodeQR[0].data.decode('ascii')
split = split.split(" ")
qrcode_answer = split[3]
send_form = {"metu" :qrcode_answer}
response = formulaire.post(url=url_challenge, data=send_form, cookies=formulaire.cookies.get_dict())
print(f"The HTML CODE {x}\n")
print(response.text)
