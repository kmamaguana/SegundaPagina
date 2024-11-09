# 🧮 Basic Calculator with Streamlit

## 📜 Description

This project consists of a **Basic Calculator** created using **Streamlit**, a Python tool for building interactive web applications easily. The application allows users to perform basic arithmetic operations like **addition**, **subtraction**, **multiplication**, and **division**.

## 🔧 Features

- ➕ **Addition**: Adds two numbers.
- ➖ **Subtraction**: Subtracts the second number from the first.
- ✖️ **Multiplication**: Multiplies two numbers.
- ➗ **Division**: Divides the first number by the second (with error handling in case of division by 0).

## 💻 Technologies Used

- **Python 3.12**
- **Streamlit**: Framework used for the web interface.

## 🛠️ Requirements

To run this project, you will need Python 3 and the necessary dependencies installed. If you don't have a virtual environment, it's recommended to create one.

### 📥 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/kmamaguana/SegundaPagina
   ```

2. Navigate to the project directory:
   ```bash
   cd calculadora-streamlit
   ```

3. (Optional) Create a virtual environment to install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use venv\Scripts\activate
   ```

4. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Running the Application

To run the calculator application, use the following command:

```bash
streamlit run app.py
```

This will open the application in your default browser at `http://localhost:8501`. 🌐

## 🐳 Dockerization

This project is dockerized for easier deployment in any environment. Follow the steps below to build and run the Docker container:

### 🏗️ Building the Docker Image

1. Build the Docker image:
   ```bash
   docker build -t calculadora-streamlit .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 8501:8501 calculadora-streamlit
   ```

This will run the application inside a container, accessible at `http://localhost:8501`. 🖥️

## 📤 Pushing to Docker Hub (Optional)

If you want to share the Docker container, you can push it to **Docker Hub**:

1. Log in to Docker Hub:
   ```bash
   docker login
   ```

2. Tag the image:
   ```bash
   docker tag calculadora-streamlit your_username/calculadora-streamlit
   ```

3. Push the image:
   ```bash
   docker push your_username/calculadora-streamlit
   ```

## 🤝 Contributing

If you'd like to contribute to this project, feel free to fork it and submit a pull request with your improvements. 🙌

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for more details. 📜

## 🙏 Thanks

A big thank you to everyone who has supported and contributed to this project! Your help and feedback are always appreciated. 🙏

![Minion](https://octodex.github.com/images/minion.png)
