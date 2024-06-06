import openai
from dotenv import load_dotenv
import os

load_dotenv()

def get_tests(code, test_framework):
  # Access the environment variables from the .env file
  api_key = os.environ.get('OPENAI_API_KEY')

  openai.api_key = api_key

  if test_framework == "pytest":
    prompt = "Generate unit test using pytest for the functions defined in next code. First you must remove all comments that appear in the code:" + code 
  elif test_framework == "unittest":
    prompt = "Generate unit test using unittest for the functions defined in next code. First you must remove all comments that appear in the code:   " + code 
  else:
    raise ValueError("El framework de test especificado no es válido. Debe ser 'pytest' o 'unittest'.")

  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You must give me only python code, I don't need any text reply, explication or comment"},
      {"role": "user", "content": prompt}
    ]
  )

  print(completion.choices[0].message.content)
  codigo = completion.choices[0].message.content
  return codigo

def get_contenido_error(code, error):
  # Access the environment variables from the .env file
  api_key = os.environ.get('OPENAI_API_KEY')

  openai.api_key = api_key
  client = openai.OpenAI()


  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You can only give me python code"},
      {"role": "user", "content": f"Executing next code: ```{code}```. I found this error: {error}. You must return the correct code without explications or comments"}
    ]
  )

  print(completion.choices[0].message.content)
  codigo = completion.choices[0].message.content
  return codigo

def get_tests_error(code, error):
  # Access the environment variables from the .env file
  api_key = os.environ.get('OPENAI_API_KEY')

  openai.api_key = api_key
  


  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You can only give me python code"},
      {"role": "user", "content": f"Executing next code: ```{code}```. I found this error: {error}. You must return the correct code without explications or comments"}
    ]
  )

  print(completion.choices[0].message.content)
  codigo = completion.choices[0].message.content
  return codigo