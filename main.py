

import google.generativeai as genai

# Cole aqui sua API do google, caso nao tenha voce pode pegar em https://aistudio.google.com/app/apikey
genai.configure(api_key="GOOGLE_API_KEY")

# Set up the model
generation_config = {
  "candidate_count": 1,
  "temperature":0.5,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

# Você pode executar este comando para listar quais modelos de linguagem estão disponíveis
# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)

model = genai.GenerativeModel(
  model_name="MODEL_NAME",
  generation_config=generation_config,
  safety_settings=safety_settings
)

chat = model.start_chat(history=[])

prompt = input("Digite algo: ")

while prompt != "Fim":
  response = chat.send_message(prompt)
  print("Aqui esta sua resposta", response.text, "\n")
  print("Para finalizar digite Fim")
  prompt = input("Digite algo")

