import streamlit as st
import numpy as np
import pandas as pd
import time

# 1. Page Configuration
st.set_page_config(page_title="Thermodynamics Property Finder", layout="wide")

# 2. Advanced CSS with Lightning Flash Animation
st.markdown("""
    <style>
    /* Background */
    .stApp {
        background-color: #0a0c10;
        background-image: linear-gradient(rgba(10, 12, 16, 0.8), rgba(10, 12, 16, 0.8)),
            url('https://www.transparenttextures.com/patterns/carbon-fibre.png');
    }

    /* Horizontal Lightning Flash Animation */
    @keyframes lightning-strike {
        0% { width: 0%; opacity: 0; left: 50%; }
        20% { width: 100%; opacity: 1; left: 0%; box-shadow: 0 0 20px #00f0ff, 0 0 40px #4a90e2; }
        40% { opacity: 0.3; }
        60% { opacity: 1; box-shadow: 0 0 30px #ffffff; }
        100% { width: 100%; opacity: 0; left: 0%; }
    }

    .lightning-bolt {
        height: 4px;
        background: white;
        position: relative;
        margin: 10px 0;
        border-radius: 2px;
        animation: lightning-strike 0.6s ease-out forwards;
        z-index: 99;
    }

    /* Main Container */
    .main-box {
        border: 2px solid #4a90e2;
        border-radius: 15px;
        background: rgba(15, 18, 25, 0.8);
        box-shadow: 0 0 20px rgba(74, 144, 226, 0.3);
        padding: 20px;
        margin-top: 20px;
    }

    /* Result Box - BOLD Text */
    .result-text {
        font-weight: 900 !important;
        font-size: 22px !important;
        color: #ffffff !important;
        background-color: #28a745;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        border: 2px solid #1e7e34;
        box-shadow: 0 0 15px rgba(40, 167, 69, 0.5);
        margin-top: 20px;
    }

    /* Calculate Button */
    .stButton > button {
        background: radial-gradient(circle, #ff4b4b 0%, #a50000 100%) !important;
        color: white !important;
        border-radius: 8px !important;
        width: 100% !important;
        height: 55px !important;
        font-weight: bold !important;
        font-size: 18px !important;
        border: 2px solid #222 !important;
        text-transform: uppercase;
    }

    .turbine-blade { font-size: 50px; animation: rotate 2s linear infinite; display: inline-block; color: #d4af37; }
    @keyframes rotate { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    </style>
    """, unsafe_allow_html=True)

# 3. Header
st.markdown('<div style="border: 2px solid #4a90e2; padding: 10px; border-radius: 12px; text-align: center; background: rgba(74, 144, 226, 0.1);"> <h1 style="color:#4a90e2; margin:0;">Thermodynamics Property Finder</h1></div>', unsafe_allow_html=True)
st.write(f"<p style='text-align:center; color:#d4af37; font-weight:bold;'>Created by: Ramish Ali | Reg. No: 25-ME-87</p>", unsafe_allow_html=True)

# 4. Sidebar
st.sidebar.title("Industrial Dashboard")
st.sidebar.markdown('<div style="text-align:center;"><div class="turbine-blade">⚙️</div><p style="color:#d4af37; font-weight:bold;">TURBINE ACTIVE</p></div>', unsafe_allow_html=True)

# 5. Main UI
st.markdown('<div class="main-box">', unsafe_allow_html=True)
col1, mid, col2 = st.columns([1, 0.1, 1])

with col1:
    st.markdown("### 📥 Input Parameters")
    gas_r = st.number_input("Gas Constant R (J/kg-K)", value=287.0)
    temp = st.number_input("Temperature (K)", value=300.0)
    pres = st.number_input("Pressure (Pa)", value=101325.0)
    st.write("##")
    
    calculate = st.button("CALCULATE")
    # Lightning flash placeholder
    flash_placeholder = st.empty()

with col2:
    st.markdown("### 📊 P-V Diagram Analysis")
    v = np.linspace(0.1, 1.0, 50)
    p = (gas_r * temp) / v
    st.line_chart(pd.DataFrame({'Volume': v, 'Pressure': p}).set_index('Volume'))

st.markdown('</div>', unsafe_allow_html=True)

# 6. Action on Press
if calculate:
    # 1. Show Lightning Flash
    flash_placeholder.markdown('<div class="lightning-bolt"></div>', unsafe_allow_html=True)
    time.sleep(0.1) # Choti si delay taaki flash nazar aaye
    
    # 2. Calculation
    density = pres / (gas_r * temp)
    
    # 3. Display Bold Result
    result_html = f"""
    <div class="result-text">
        ANALYSIS COMPLETE! FLUID DENSITY: <b>{density:.4f} kg/m³</b>
    </div>
    """
    st.markdown(result_html, unsafe_allow_html=True)
