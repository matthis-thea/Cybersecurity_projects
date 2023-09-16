#coding:utf-8
import  socket
import  math
import  base64
import  codecs

# Variables
IP = "challenge01.root-me.org"
Port = 52021

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("You are connected : " + IP)

irc.connect((IP, Port))

while True:
    text = irc.recv(1024).decode()
    print(text)
    liste = text.split("\n")
    word = " "
    for x in liste:
        word = x
        if (word.find("my") != -1):
            chaine = word.split(" ")
            final = chaine[3]
            test = final.split("'")
            final = test[1]
            str_example = codecs.decode(final, 'rot_13') + "\n"
            irc.send(bytes(str_example, "UTF-8"))
    if (text.find("flag") != -1):
        exit(0)