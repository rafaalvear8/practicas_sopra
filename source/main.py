import streamlit as st
import openai
import requests
import test
from dotenv import load_dotenv
import os
from io import StringIO
import contextlib
load_dotenv()

# Configurar la API de OpenAI
api_key = os.environ.get('OPENAI_API_KEY')
openai.api_key = api_key


# Título de la aplicación
st.title('Generador de tests unitarios mediante IA Generativa')

# Información de autores y tutor
st.header('Autores:')
st.write('''
- Rafael Alvear  
- Samuel Burgueño
''')
st.write('Tutor: Pablo Guijarro')

# Selector de framework de prueba
test_framework = st.radio("Selecciona el framework para generar los tests:", ("pytest", "unittest"))

def eliminar_caracteres_innecesarios(codigo):
    """
    Elimina caracteres innecesarios del código.

    Args:
        codigo (str): El código del cual se eliminarán los caracteres innecesarios.

    Returns:
        str: El código sin los caracteres innecesarios.
    """
    codigo = codigo.replace("```", "")
    codigo = codigo.replace("python", "")
    return codigo

def obtener_contenido_archivo_desde_github(url):
    """
    Obtiene el contenido de un archivo desde un repositorio de GitHub.

    Args:
        url (str): La URL del archivo en el repositorio de GitHub.

    Returns:
        str: El contenido del archivo.
    """
    raw_url = url.replace("github.com", "raw.githubusercontent.com")
    # Reemplaza '/blob/' por '/' en la URL para obtener el enlace directo al archivo
    raw_url = raw_url.replace("/blob/", "/")
    response = requests.get(raw_url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def ejecutar_tests(test_code):
    """
    Ejecuta los tests generados y captura los resultados.

    Args:
        test_code (str): El código de los tests a ejecutar.

    Returns:
        str: Los resultados de la ejecución de los tests.
    """
    print("Código de los tests:")
    print(test_code)
    
    # Capturar la salida estándar durante la ejecución de los tests
    stdout = StringIO()
    with contextlib.redirect_stdout(stdout):
        try:
            exec(test_code)
            return "Los tests se ejecutaron correctamente."
        except SyntaxError as e:
            print("Error de sintaxis al ejecutar los tests:", e)
            return f"Error de sintaxis al ejecutar los tests: {e}"
        except ModuleNotFoundError as e:
            print("No se pueden ejecutar tests con dependencias externas.")
            return "No se pueden ejecutar tests con dependencias externas."
        except Exception as e:
            print("Error al ejecutar los tests:", e)
            return f"Error al ejecutar los tests: {e}"
    
   

def main():
    """
    Función principal que controla la lógica de la aplicación de Streamlit.

    Crea pestañas para ingresar una URL de repositorio o cargar un archivo Python,
    y genera tests unitarios basados en el contenido proporcionado.
    """
    # Crear pestañas
    tab1, tab2 = st.tabs(["Ingresar URL del repositorio", "Subir archivo Python"])
    with tab1:
        st.header("Generar y ejecutar tests unitarios desde una URL de repositorio en GitHub")
        
        # Inputs para que el usuario ingrese los detalles del repositorio y el archivo
        path = st.text_input("Ingresa la URL del repositorio:")
        
        # Botón para obtener y mostrar el contenido del archivo
        if st.button("Generar tests unitarios para el repositorio de GitHub"):
            with st.spinner('Generando tests unitarios...'):
                if path:
                    contenido = obtener_contenido_archivo_desde_github(path)
                    if contenido:
                        tests_openai = test.get_tests(contenido, test_framework)
                        test_unitario = eliminar_caracteres_innecesarios(tests_openai)

                        # Mostrar el contenido en un componente de Streamlit
                        st.code(test_unitario, language="python")

                        # Ejecutar los tests y mostrar los resultados
                        st.header("Resultados de los tests generados:")
                        resultados = ejecutar_tests(test_unitario)
                        st.text(resultados)
                        if "correctamente" in resultados.lower():
                            st.success("¡Enhorabuena, tu código ha pasado los tests!")
                    else:
                        st.error("No se pudo obtener el contenido del archivo. Verifica los detalles del repositorio y la ruta del archivo.")
                else:
                    st.warning("Por favor, ingresa la URL del repositorio.")
    
    with tab2:
        st.header("Generar y ejecutar tests unitarios desde un archivo Python")
        
        # Caja de carga para el archivo .py
        uploaded_file = st.file_uploader("O adjunta tu archivo de Python aquí:")
        
        # Botón para generar el test unitario
        if uploaded_file is not None:
            code = uploaded_file.getvalue().decode("utf-8")
            st.write('Comprueba que el fichero subido es correcto:')
            st.code(code, language="python")
            if st.button('Generar tests unitarios'):
                with st.spinner('Generando tests unitarios...'):
                    tests_openai = test.get_tests(code, test_framework)
                    test_unitario = eliminar_caracteres_innecesarios(tests_openai)
                    # Mostrar el contenido en un componente de Streamlit
                    st.write('Test Unitario generado:')
                    st.code(test_unitario, language="python")
                    
                    # Ejecutar los tests y mostrar los resultados
                    st.header("Resultados de los tests generados:")
                    resultados = ejecutar_tests(test_unitario)
                    st.text(resultados)
                    if "correctamente" in resultados.lower():
                        st.success("¡Enhorabuena, tu código ha pasado los tests!")

if __name__ == "__main__":
    main()
