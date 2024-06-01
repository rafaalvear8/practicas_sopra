import openai
from dotenv import load_dotenv
import os

load_dotenv()

def get_tests(code):
  # Access the environment variables from the .env file
  api_key = os.environ.get('OPENAI_API_KEY')

  openai.api_key = api_key


  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "Solamente puedes devolver código en python"},
      {"role": "user", "content": "Genera la clase de tests unitarios para las funciones definidas en el siguiente código: " + code}
    ]
  )

  print(completion.choices[0].message.content)
  codigo = completion.choices[0].message.content
  return codigo