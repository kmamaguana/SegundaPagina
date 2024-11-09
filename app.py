import streamlit as st
st.image("https://cdn.dribbble.com/users/104417/screenshots/1884219/media/4324442fcf31610be2eb5e5740bd756e.gif")
st.title("Calculadora Básica")
num1 = st.number_input("Número 1", min_value=0.0)
num2 = st.number_input("Número 2", min_value=0.0)
operation = st.selectbox("Selecciona una operación", ["Suma", "Resta", "Multiplicación", "División"])
if st.button("Calcular"):
    if operation == "Suma":
        result = num1 + num2
    elif operation == "Resta":
        result = num1 - num2
    elif operation == "Multiplicación":
        result = num1 * num2
    elif operation == "División":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: División por 0"

    st.write(f"Resultado: {result}")
