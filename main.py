from random import random
import random
from discord import SyncWebhook
import requests

url = "https://discordapp.com/api/webhooks/1054497636062863420/3_BLqqfnCYvr7leTq8oGjr-VHKkD6vrntZLdXz_YHPCQQR14azemWzNbcUg-dgKN_EfV"


data = {
    "content" : "",
    "username" : "Sorteio"
}


fileobj=open("teams.txt")
teams=[]
for team in fileobj:
    teams.append(team.strip())
print(teams)


fileobj1=open("users.txt")
users=[]
for user in fileobj1:
    users.append(user.strip())
print(users)
print("\n")


valUsers = len(users)
valTeams = len(teams)

if valTeams < valUsers:
 print("Reveja o numero de equipas (Existem mais Treinadores do que equipas")

else:
 i = 0
 while i < valUsers:
  random_user = random.choice(users)
  random_team = random.choice(teams)
  print("-----------------------------------------------------------------------------")
  print("o jogador " + str(random_user) + " vai treinar o clube: " + str(random_team))
  print("-----------------------------------------------------------------------------")
  print("\n")
  users.remove(random_user)
  teams.remove(random_team)

  data["embeds"] = [
   {
    "description": f'JOGADOR: {random_user}\n' + f'EQUIPA: {random_team}\n'  ,

    "title": "jogador/equipa"
   }
  ]

  result = requests.post(url, json=data)

  try:
   result.raise_for_status()
  except requests.exceptions.HTTPError as err:
   print(err)
  else:
   print("Payload delivered successfully, code {}.".format(result.status_code))

  i += 1




print("\n")
print(" Sorteio Finalizado")




