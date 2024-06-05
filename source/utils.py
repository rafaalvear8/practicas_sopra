import streamlit as st


def descargar_archivo_contenido(file_name, content):
    """
    Muestra un botón de descarga en Streamlit para descargar un archivo con el contenido generado.

    Args:
        file_name (str): El nombre del archivo que se descargará.
        content (str): El contenido del archivo a descargar.

    Returns:
        None
    """
    st.download_button(
        label="Descargar test generado como archivo .py",
        data=content,
        file_name=file_name,
        mime='text/plain'
    )