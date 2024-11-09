# 🧮 Calculadora Básica con Streamlit

## 📜 Descripción

Este proyecto consiste en una **Calculadora Básica** creada utilizando **Streamlit**, una herramienta de Python para construir aplicaciones web interactivas de forma sencilla. La aplicación permite al usuario realizar operaciones aritméticas básicas como **suma**, **resta**, **multiplicación** y **división**.

## 🔧 Funcionalidades

- ➕ **Suma**: Suma dos números.
- ➖ **Resta**: Resta el segundo número al primero.
- ✖️ **Multiplicación**: Multiplica dos números.
- ➗ **División**: Divide el primer número por el segundo (con manejo de error en caso de división por 0).

## 💻 Tecnologías utilizadas

- **Python 3.12**
- **Streamlit**: Framework utilizado para la interfaz web.

## 🛠️ Requisitos

Para ejecutar este proyecto, necesitarás tener instalado Python 3 y las dependencias necesarias. Si no tienes un entorno virtual, te recomiendo crear uno.

### 📥 Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/calculadora-streamlit.git
   ```

2. Navega al directorio del proyecto:
   ```bash
   cd calculadora-streamlit
   ```

3. (Opcional) Crea un entorno virtual para instalar las dependencias:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa venv\Scripts\activate
   ```

4. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Ejecución

Para ejecutar la aplicación de la calculadora, usa el siguiente comando:

```bash
streamlit run app.py
```

Esto abrirá la aplicación en tu navegador por defecto en `http://localhost:8501`. 🌐

## 🐳 Dockerización

Este proyecto está dockerizado para facilitar su despliegue en cualquier entorno. Sigue los pasos a continuación para construir y ejecutar el contenedor Docker:

### 🏗️ Construcción de la imagen Docker

1. Construye la imagen de Docker:
   ```bash
   docker build -t calculadora-streamlit .
   ```

2. Ejecuta el contenedor Docker:
   ```bash
   docker run -p 8501:8501 calculadora-streamlit
   ```

Esto permitirá ejecutar la aplicación dentro de un contenedor, accesible en `http://localhost:8501`. 🖥️

## 📤 Subir a Docker Hub (Opcional)

Si deseas compartir el contenedor Docker, puedes subirlo a **Docker Hub**:

1. Inicia sesión en Docker Hub:
   ```bash
   docker login
   ```

2. Taggea la imagen:
   ```bash
   docker tag calculadora-streamlit tu_usuario/calculadora-streamlit
   ```

3. Sube la imagen:
   ```bash
   docker push tu_usuario/calculadora-streamlit
   ```

## 🤝 Contribuciones

Si deseas contribuir a este proyecto, siéntete libre de hacer un fork y enviar un pull request con tus mejoras. 🙌

## 📝 Licencia

Este proyecto está licenciado bajo la **MIT License** - consulta el archivo [LICENSE](LICENSE) para más detalles. 📜

