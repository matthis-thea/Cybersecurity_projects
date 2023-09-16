#coding:utf-8
import  socket
import  math

# Variables
IP = "challenge01.root-me.org"
Port = 52018

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("You are connected : " + IP)

irc.connect((IP, Port))

while True:
    result = irc.recv(1024).decode()
    print(result)
    result_split = result.split("\n")
    for x in result_split:
        if x.find("Solve this equation please") != -1:
            result_find = x
            equation_split = result_find.split(" ")
            equation_a = equation_split[6]
            equation_b = equation_split[8] 
            equation_c = float(equation_split[10])
            
            equation_split = equation_a.split(".")
            equation_a = float(equation_split[0])
            equation_split = equation_b.split(".")
            equation_b = float(equation_split[0])
    delta = equation_b**2 - 4*equation_a*equation_c

    # Si delta est négatif
    if(delta < 0):
          resultat = "Not possible"
          irc.send(bytes(resultat, "UTF-8"))
    # Sinon, delta peut être positif ou nul    
    else:
        # Si delta est nul
        if (delta == 0):
            print("L'équation equation_a une solution double.")
            x = -equation_b / (2.*equation_a)
            print ("La solution est x = ",x)
        
        #Sinon,  delta ne peut plus qu'être positif.
        else:
            print("L'équation equation_a deux solutions solutions.")
            x1 = (-equation_b - math.sqrt(delta)) /(2*equation_a)
            x2 = (-equation_b + math.sqrt(delta)) /(2*equation_a)
            print ("Les solutions sont x1 = ",x1, " et ", x2)
result = irc.recv(1024).decode()
print(result)
