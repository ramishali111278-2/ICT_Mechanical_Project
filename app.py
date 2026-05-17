import streamlit as st
import numpy as np
import pandas as pd

# Page configuration
st.set_page_config(page_title="Thermodynamics Property Finder", layout="wide")

# Custom CSS for Industrial/Mechanical Look
st.markdown("""
    <style>
    .main {
        background-color: #1e2130;
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 50%;
        width: 120px;
        height: 120px;
        border: 4px solid #333;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(255, 75, 75, 0.4);
        margin: 0 auto;
        display: block;
    }
    .stButton>button:hover {
        background-color: #ff0000;
        border-color: #fff;
    }
    .header-box {
        background: linear-gradient(90deg, #d4af37, #f9f295, #d4af37);
        padding: 10px;
        border-radius: 5px;
        text-align: center;
        color: #333;
        font-weight: bold;
        border: 2px solid #8a6d3b;
    }
    .metric-card {
        background-color: #2b2e42;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #d4af37;
    }
    </style>
    """, unsafe_allow_html=True)

# Title Section
st.markdown("<h1 style='text-align: center; color: #4a90e2;'>Thermodynamics Property Finder</h1>", unsafe_allow_html=True)
st.markdown('<div class="header-box">Ramish Ali / 25-ME-87</div>', unsafe_allow_html=True)

st.write("## Ideal Gas Property Calculator")

# Layout with Columns
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    R = st.number_input("Gas Constant R (J/kg-K)", value=287.0)
    T = st.number_input("Temperature (K)", value=300.0)
    P = st.number_input("Pressure (Pa)", value=101325.0)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("##")
    # Big Circular Calculate Button
    calculate = st.button("CALCULATE")

with col2:
    # Adding a dummy P-V curve graph
    st.write("### P-V Diagram Analysis")
    volume = np.linspace(0.1, 1.0, 100)
    # Ideal gas law: P = nRT/V (Assuming nR is constant for visualization)
    pressure_curve = (R * T) / volume
    
    chart_data = pd.DataFrame({
        'Volume (m3)': volume,
        'Pressure (Pa)': pressure_curve
    })
    st.line_chart(chart_data.set_index('Volume (m3)'))

# Calculation Logic
if calculate:
    density = P / (R * T)
    specific_volume = 1 / density
    
    st.divider()
    res_col1, res_col2 = st.columns(2)
    res_col1.metric("Density (ρ)", f"{density:.4f} kg/m³")
    res_col2.metric("Spec. Volume (v)", f"{specific_volume:.4f} m³/kg")
    st.balloons()

st.sidebar.title("Industrial Gadgets")
st.sidebar.info("System Status: Online 🟢")
st.sidebar.write("Pressure Gauge: Active")
st.sidebar.write("Turbine RPM: 3500")
