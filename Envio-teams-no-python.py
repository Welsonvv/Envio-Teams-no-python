import time
import os
import sys
import requests
import pandas as pd
from datetime import datetime as dt,timedelta

############  Informações da rotina para envia via teams #######
rotina = "Nome da rotina"
Detalhes ='detalhes'
################################################################


def enviar_teams(rotina):
 
    # Capturar o nome do script
    nome_script = os.path.basename(sys.argv[0])
  # Dados a serem enviados na requisição POST
    data_teams = {
        "rotina": rotina,
        "detalhes": rotina,
        "script_job": nome_script,
        "tempo_exec": "00:00:00",
        "erro": "0 Erro(s)",
        "obs": ""
    }
     # URL para enviar a requisição Producao
    url_teams = ""
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.post(url_teams, json=data_teams, headers=headers)
  #  response2 = requests.post(url_teams2, json=data_teams, headers=headers)

    if response.status_code in (200, 202):
        print("Requisição enviada com sucesso!")
        print(response.text)
    else:
        print(f"Erro {response.status_code} ao enviar a requisição:")
        print("Resposta:", response.text)

enviar_teams(rotina)