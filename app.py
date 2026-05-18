import streamlit as st
import numpy as np
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="Thermodynamics Property Finder", layout="wide")

# 2. Advanced CSS - Partition and Button fix
st.markdown("""
    <style>
    /* Background */
    .stApp {
        background-color: #0a0c10;
        background-image: linear-gradient(rgba(10, 12, 16, 0.8), rgba(10, 12, 16, 0.8)),
            url('https://www.transparenttextures.com/patterns/carbon-fibre.png');
    }

    /* Main Container with Partition */
    .main-border-box {
        border: 2px solid #4a90e2;
        border-radius: 15px;
        background: rgba(15, 18, 25, 0.7);
        box-shadow: 0 0 15px rgba(74, 144, 226, 0.3);
        display: flex;
        padding: 0;
        overflow: hidden;
        margin-bottom: 20px;
    }

    /* Vertical Partition Line */
    .partition-line {
        width: 2px;
        background: linear-gradient(to bottom, transparent, #4a90e2, transparent);
        margin: 20px 0;
    }

    .column-content {
        padding: 25px;
        flex: 1;
    }

    /* Box Header Animation */
    .box-header-line {
        height: 3px;
        width: 100%;
        background: linear-gradient(90deg, transparent, #00f0ff, #0072ff, transparent);
        animation: neon-glow 2s linear infinite;
    }

    @keyframes neon-glow {
        0% { background-position: -200% 0; }
        100% { background-position: 200% 0; }
    }

    /* Turbine Animation */
    .turbine-container { text-align: center; padding: 10px; }
    .turbine-blade { font-size: 50px; animation: rotate 2s linear infinite; display: inline-block; color: #d4af37; }
    @keyframes rotate { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }

    /* Red Calculate Button - Full Text */
    .stButton > button {
        background: radial-gradient(circle, #ff4b4b 0%, #a50000 100%) !important;
        color: white !important;
        border-radius: 10px !important; /* Slightly rounded for better text fit */
        width: 100% !important;
        height: 50px !important;
        font-weight: bold !important;
        font-size: 18px !important;
        border: 2px solid #222 !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .title-box {
        border: 2px solid #4a90e2;
        padding: 10px;
        border-radius: 12px;
        text-align: center;
        background: rgba(74, 144, 226, 0.1);
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Header
st.markdown('<div class="title-box"><h1 style="color:#4a90e2; margin:0;">Thermodynamics Property Finder</h1></div>', unsafe_allow_html=True)
st.write(f"<p style='text-align:center; color:#d4af37; font-weight:bold;'>Created by: Ramish Ali | Reg. No: 25-ME-87</p>", unsafe_allow_html=True)

# 4. Sidebar
st.sidebar.title("Industrial Dashboard")
st.sidebar.markdown('<div class="turbine-container"><div class="turbine-blade">⚙️</div><p style="color:#d4af37; font-weight:bold;">TURBINE ACTIVE</p></div>', unsafe_allow_html=True)

# 5. Main UI with Partition
st.markdown('<div class="box-header-line"></div>', unsafe_allow_html=True)

# Custom Layout using Streamlit Columns inside the styled area
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📥 Input Parameters")
    gas_r = st.number_input("Gas Constant R (J/kg-K)", value=287.0)
    temp = st.number_input("Temperature (K)", value=300.0)
    pres = st.number_input("Pressure (Pa)", value=101325.0)
    st.write("##")
    calculate = st.button("CALCULATE") # Poora naam likha hai

with col2:
    # Column 2 ke shuru mein partition line effect ke liye space
    st.markdown("### 📊 P-V Diagram Analysis")
    v = np.linspace(0.1, 1.0, 50)
    p = (gas_r * temp) / v
    chart_data = pd.DataFrame({'Volume': v, 'Pressure': p}).set_index('Volume')
    st.line_chart(chart_data, use_container_width=True)

# 6. Results
if calculate:
    density = pres / (gas_r * temp)
    st.success(f"Analysis Complete! Fluid Density: **{density:.4f} kg/m³**")
