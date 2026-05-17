import streamlit as st

# Custom title with color
st.markdown("<h1 style='color:blue;text-align:center;'>Thermodynamics Property Finder</h1>", unsafe_allow_html=True)

# Developer info with styled box
st.markdown(
    "<div style='background-color:#f9f9a7;padding:10px;border-radius:8px;text-align:center;'>"
    "Developed by <b style='color:green;'>Ramish Ali</b>, Roll: <b style='color:red;'>25-ME-87</b>"
    "</div>",
    unsafe_allow_html=True
)

st.header("Ideal Gas Property Calculator")

# Layout with columns
col1, col2 = st.columns(2)

with col1:
    gas_constant = st.number_input("Gas Constant R (J/kg·K)", value=287.0)

with col2:
    temperature = st.number_input("Temperature (K)", value=300.0)

pressure = st.number_input("Pressure (Pa)", value=101325.0)

# Calculate button
if st.button("Calculate Properties"):
    density = pressure / (gas_constant * temperature)
    specific_volume = 1 / density

    # Styled results
    st.markdown(
        f"<h3 style='color:purple;'>Density: {density:.3f} kg/m³</h3>",
        unsafe_allow_html=True
    )
    st.markdown(
        f"<h3 style='color:orange;'>Specific Volume: {specific_volume:.6f} m³/kg</h3>",
        unsafe_allow_html=True
    )
