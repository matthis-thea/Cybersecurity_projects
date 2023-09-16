#coding:utf-8
import  socket
import  math

# Variables
IP = "challenge01.root-me.org"
Port = 52002

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
        if (word.find("Calculate") != -1):
            chaine = word.split(" ")
            final = chaine[5]
            final_two = chaine[9]
            result = math.sqrt(float(final)) * float(final_two)
            result = round(result, 2)
            final_result = str(result) + "\r\n"
            irc.send(bytes(final_result, "UTF-8"))
    if (text.find("flag") != -1):
        exit(0)