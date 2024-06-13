# Proyecto de Prácticas de Empresa con OpenAI

Este repositorio contiene el código desarrollado para las prácticas de empresa en el contexto del uso de la API de OpenAI para generar tests con una complejidad incremental. El objetivo principal de este proyecto es explorar el potencial de la inteligencia artificial en el ámbito de la generación automatizada de tests unitarios.

## Descripción del Proyecto

El proyecto se centra en el desarrollo de un sistema que utilice la API de OpenAI para generar tests unitarios para funciones y métodos específicos de un proyecto de software. Estos tests serán generados de manera incremental, comenzando desde casos simples y aumentando gradualmente en complejidad.

## Requisitos del Sistema

- Python 3.x
- Paquete de OpenAI (instalable mediante `pip install openai`)
- Cuenta y API Key de OpenAI (necesaria para acceder a la API)

## Instalación

Sigue estos pasos para configurar el entorno de desarrollo:

1. Clona el repositorio:

`git clone https://github.com/sabufu/practicas_sopra.git`

2. Crea y activa un entorno virtual (opcional pero recomendado):

`python -m venv venv`
`source venv/bin/activate`  # En Windows usa `venv\Scripts\activate`


3. Instala las dependencias:

`pip install -r requirements.txt`


## Uso

Para utilizar este sistema, sigue estos pasos:

1. Clona este repositorio en tu máquina local.
2. Instala las dependencias utilizando `pip install -r requirements.txt`.
3. Obtén tu API Key de OpenAI y configúrala en el archivo `.env`.
4. Ejecuta el script principal para comenzar a generar tests unitarios utilizando el siguiente comando `streamlit run source/main.py`



## Contribución

¡Las contribuciones son bienvenidas! Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Haz tus cambios y haz commit de ellos (`git commit -am 'Añade nueva característica'`).
4. Haz push de la rama (`git push origin feature/nueva-caracteristica`).
5. Abre un Pull Request.

## Contacto

Para cualquier pregunta o sugerencia, no dudes en ponerte en contacto con el equipo de desarrollo en alveargp10@gmail.com o samuguiel@gmail.com.
