import streamlit as st
import openai
import requests
from dotenv import load_dotenv
import os
import test

load_dotenv()

# Configurar la API de OpenAI
api_key = os.environ.get('OPENAI_API_KEY')

openai.api_key = api_key

# Crear una fila para los logos en la esquina superior izquierda
col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    st.image('../images/soprasteria_logo.jpg', width=100)
with col3:
    st.image('../images/unir_universidad_internet_logo.jpg', width=100)

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
    codigo = codigo.replace("```", "")
    codigo = codigo.replace("python", "")
    return codigo



def obtener_contenido_archivo_desde_github(url):
    raw_url = url.replace("github.com", "raw.githubusercontent.com")
    # Reemplaza '/blob/' por '/' en la URL para obtener el enlace directo al archivo
    raw_url = raw_url.replace("/blob/", "/")
    response = requests.get(raw_url)
    if response.status_code == 200:
        return response.text
    else:
        return None
    



def main():
    # Crear pestañas
    tab1, tab2 = st.tabs(["Ingresar URL del repositorio", "Subir archivo Python"])

    with tab1:
        st.header("Generar tests unitarios desde una URL de repositorio en GitHub")
        
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

                                               # Botón de descarga
                        st.download_button(
                            label="Descargar test generado como archivo .py",
                            data=test_unitario,
                            file_name='test_unitario_generado.py',
                            mime='text/plain'
                        )
                    else:
                        st.error("No se pudo obtener el contenido del archivo. Verifica los detalles del repositorio y la ruta del archivo.")
                else:
                    st.warning("Por favor, ingresa la URL del repositorio.")
    
    with tab2:
        st.header("Generar tests unitarios desde un archivo Python")
        
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
                    
                
                    
                    # Botón de descarga
                    st.download_button(
                        label="Descargar test generado como archivo .py",
                        data=test_unitario,
                        file_name='test_unitario_generado.py',
                        mime='text/plain'
                    )

                

if __name__ == "__main__":
    main()