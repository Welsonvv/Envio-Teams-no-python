# 📢 Envio de Notificações para Microsoft Teams com Python e Power Automate

Este projeto automatiza o envio de mensagens para um canal ou chat do **Microsoft Teams** usando um script em Python e um fluxo no **Power Automate**.

---

## 🚀 Objetivo

Automatizar alertas, notificações ou logs de execução de rotinas (como ETL, jobs e scripts) enviando mensagens diretamente para o Microsoft Teams.

---

## 🧰 Pré-requisitos

- Conta Microsoft com acesso ao Microsoft Teams
- Acesso ao [Power Automate](https://make.powerautomate.com/)
- Python 3.7 ou superior
- Bibliotecas:
  - `requests`
  - `pandas` (opcional no envio, usada na rotina principal)

---

## ⚙️ Configuração do Power Automate

### 1. Criar o Fluxo

1. Acesse o Power Automate: [https://make.powerautomate.com/](https://make.powerautomate.com/)
2. Clique em **Criar** > **Automatizado a partir de um gatilho em branco**
3. Escolha o gatilho: `Quando uma solicitação HTTP for recebida` (`When an HTTP request is received`)
4. Defina o schema de entrada (exemplo abaixo):

```json
{
  "type": "object",
  "properties": {
    "rotina": { "type": "string" },
    "detalhes": { "type": "string" },
    "script_job": { "type": "string" },
    "tempo_exec": { "type": "string" },
    "erro": { "type": "string" },
    "obs": { "type": "string" }
  }
}
```

5. Adicione uma nova ação: `Postar cartão adaptável no Teams`
6. Cole o JSON do Adaptive Card fornecido abaixo
7. Salve o fluxo e copie a URL do webhook gerada.

---

## 🐍 Execução do Script Python

### 1. Instale as dependências:

```bash
pip install requests pandas
```

### 2. Configure o script:

- Atualize a variável `url_teams` no Python com a URL do seu Power Automate.
- Ajuste os campos conforme a necessidade da sua rotina.

### 3. Execute o script:

```bash
python nome_do_script.py
```

Se configurado corretamente, uma mensagem será enviada ao Teams após a execução do script.

---

## 📂 Estrutura Esperada

```
.
├── envio_teams.py
├── README.md
```

---

## ✅ Exemplo de Mensagem no Teams

```
🚨 Rotina: Nome da rotina
📄 Script: envio_teams.py
⏱️ Tempo: 00:00:00
❌ Erros: 0 Erro(s)
📝 Observações: 
```

---

## 🎨 Estrutura do Adaptive Card no Teams

Este projeto utiliza um **Adaptive Card** no Power Automate para enviar notificações visualmente organizadas no Teams.

### 🧱 Estrutura Utilizada

```json
{
  "$schema": "https://adaptivecards.io/schemas/adaptive-card.json",
  "type": "AdaptiveCard",
  "version": "1.5",
  "body": [
    {
      "type": "ColumnSet",
      "columns": [
        {
          "type": "Column",
          "width": "stretch",
          "items": [
            {
              "type": "TextBlock",
              "text": "✅ Rotina Executada",
              "weight": "Bolder",
              "size": "Large",
              "horizontalAlignment": "Left",
              "color": "Good",
              "spacing": "Medium"
            }
          ]
        }
      ],
      "spacing": "None"
    },
    {
      "type": "Container",
      "spacing": "Medium",
      "items": [
        {
          "type": "FactSet",
          "facts": [
            {
              "title": "🛠️ Rotina:",
              "value": "@{triggerBody()?['Rotina']}"
            },
            {
              "title": "📋 Detalhes:",
              "value": "@{triggerBody()?['detalhes']}"
            },
            {
              "title": "📄 Script/Job:",
              "value": "@{triggerBody()?['script_job']}"
            },
            {
              "title": "⏱️ Tempo de Exec:",
              "value": "@{triggerBody()?['tempo_exec']}"
            },
            {
              "title": "❌ Erro:",
              "value": "@{triggerBody()?['erro']}"
            }
          ]
        },
        {
          "type": "TextBlock",
          "text": "💬 Obs:",
          "weight": "Bolder",
          "spacing": "Small"
        },
        {
          "type": "TextBlock",
          "wrap": true,
          "maxLines": 3
        },
        {
          "type": "ActionSet",
          "actions": [
            {
              "type": "Action.ShowCard",
              "title": "➕ Ver mais",
              "card": {
                "type": "AdaptiveCard",
                "body": [
                  {
                    "type": "TextBlock",
                    "text": "@{triggerBody()?['obs']}",
                    "wrap": true
                  }
                ],
                "$schema": "https://adaptivecards.io/schemas/adaptive-card.json",
                "version": "1.5"
              }
            }
          ],
          "spacing": "None"
        }
      ]
    }
  ]
}
```

### 🛠️ Onde usar

No Power Automate, utilize a ação:
- **"Postar um cartão adaptável para um canal"** ou
- **"Postar um cartão adaptável para um chat com o Flow Bot"**

Cole o JSON acima no campo de mensagem e certifique-se de substituir os campos dinâmicos com `@{triggerBody()?['...']}`.

Você pode testar e editar seu card usando o [Adaptive Card Designer](https://adaptivecards.io/designer/).

---

## 👨‍💻 Autor

Desenvolvido por [Welson Viana](https://github.com/Welsonvv)

---

## 🛡️ Licença

MIT License
