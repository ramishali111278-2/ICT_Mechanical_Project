import streamlit as st

st.title("Thermodynamics Property Finder")

# Display your name and roll number
st.write("Developed by **Ramish Ali**, Roll: 25-ME-87")

st.header("Ideal Gas Property Calculator")

# Inputs
gas_constant = st.number_input("Enter Gas Constant R (J/kg·K)", value=287.0)
temperature = st.number_input("Enter Temperature (K)", value=300.0)
pressure = st.number_input("Enter Pressure (Pa)", value=101325.0)

if st.button("Calculate Properties"):
    # Density from Ideal Gas Law: rho = P / (R*T)
    density = pressure / (gas_constant * temperature)

    # Specific volume: v = 1 / rho
    specific_volume = 1 / density

    st.success(f"Density: {density:.3f} kg/m³")
    st.success(f"Specific Volume: {specific_volume:.6f} m³/kg")
