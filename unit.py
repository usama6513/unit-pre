import streamlit as st

st.title("⚖⇆📏✏unit converter")
st.header("Welcome to unit converter !")

# Input fields
value = st.number_input("Enter your value you want to convert:")
unit_from = st.text_input("Enter your value you want to convert from (meters, kilometers, gram, kilogram, kilograms, pounds)")
unit_to = st.text_input("Enter your value you want to convert to (meters, kilometers, gram, kilogram, kilograms, pounds)")

# Define conversion function
def convert_unit(value: float, unit_from: str, unit_to: str):
    if unit_from == 'kilometers' and unit_to == 'meters':
        return value * 1000
    elif unit_from == 'meters' and unit_to == 'kilometers':
        return value * 0.001
    elif unit_from == 'kilograms' and unit_to == 'grams':
        return value * 1000
    elif unit_from == 'grams' and unit_to == 'kilograms':
        return value * 0.001
    elif unit_from == 'kilograms' and unit_to == 'pounds':
        return value * 2.20462
    elif unit_from == 'pounds' and unit_to == 'kilograms':
        return value * 0.453592
    else:
        return "Invalid conversion"

# Button to trigger conversion
if st.button('Convert'):
    result = convert_unit(value, unit_from, unit_to)
    st.write(f"Converted value is: {result}")  # Correct usage of st.write

