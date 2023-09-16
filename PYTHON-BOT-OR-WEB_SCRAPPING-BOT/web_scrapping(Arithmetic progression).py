#coding --utf8---
import requests
import time
formulaire = requests.Session()
def parsing():
    counter_l = 0
    counter_l2 = 0
    first_number = 0
    second_number = 0
    signe = ""
    U0 = 0
    int_max = 0
    url_html = "http://challenge01.root-me.org/programmation/ch1/"
    response_html = formulaire.get(url=url_html)
    resultat_html = response_html.text
    parsing_text = resultat_html.split('<sub>')


    for x_parse in parsing_text:
        if (counter_l == 1):
            line = x_parse
            line = line.split(" ")
            first_number = line[3]
        if (counter_l == 2):
            line = x_parse
            line = line.split(" ")
            signe = line[2]
            second_number = line[6]
        if (counter_l == 3):
            line = x_parse
            line = line.split("\n")
            for x4_parse in line:
                if (counter_l2 == 0):
                    line = x4_parse
                    line = line.split(" ")
                    U0 = line[2]
                counter_l2 = counter_l2 + 1
        if (counter_l == 4):
            line = x_parse
            line = line.split("<")
            int_max = line[0]
        counter_l = counter_l + 1
        counter_l2 = 0


    for i in range(int(int_max)):
        if (signe == '-'):
            U0 = (int(first_number) + int(U0)) - (i * int(second_number))
        else:
            U0 = (int(first_number) + int(U0)) + (i * int(second_number))


    url_destination = "http://challenge01.root-me.org/programmation/ch1/ep1_v.php?result=" + str(U0)
    response_html = requests.get(url=url_destination, cookies=formulaire.cookies.get_dict())
    print(response_html.text)

if __name__ == '__main__':
    start = time.time()
    parsing()
    end = time.time()
    difference = end - start
    print(f'Execution time : {difference}ms\n')