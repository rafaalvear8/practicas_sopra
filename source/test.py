import openai
from dotenv import load_dotenv
import os

load_dotenv()

def get_tests(code, test_framework):
  """
  Genera tests unitarios utilizando OpenAI para las funciones definidas en el código proporcionado.

  Args:
      code (str): El código de las funciones para las cuales se generarán los tests.
      test_framework (str): El framework de prueba a utilizar ("pytest" o "unittest").

  Returns:
      str: El código de los tests generados.
  """

  # Access the environment variables from the .env file
  api_key = os.environ.get('OPENAI_API_KEY')

  openai.api_key = api_key

  if test_framework == "pytest":
    prompt = "Genera los tests unitarios utilizando pytest para las funciones definidas en el siguiente código: " + code + "Devuélveme solamente código, no escribas nada de texto."
  elif test_framework == "unittest":
    prompt = "Genera los tests unitarios utilizando unittest para las funciones definidas en el siguiente código: " + code + "Devuélveme solamente código, no escribas nada de texto."
  else:
    raise ValueError("El framework de test especificado no es válido. Debe ser 'pytest' o 'unittest'.")
  

  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "Solamente puedes devolver código en python"},
      {"role": "user", "content": prompt}
    ]
  )


  print(completion.choices[0].message.content)
  codigo = completion.choices[0].message.content
  return codigo