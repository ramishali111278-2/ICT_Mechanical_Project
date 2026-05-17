import streamlit as st
import numpy as np
import pandas as pd
import time

# Page configuration
st.set_page_config(page_title="Thermodynamics Property Finder", layout="wide")

# Custom CSS for Margin Box, Profile, and Animated Turbine
st.markdown("""
    <style>
    /* Industrial Background */
    .stApp {
        background-color: #11141b;
        background-image: 
            linear-gradient(rgba(17, 20, 27, 0.9), rgba(17, 20, 27, 0.9)),
            url('https://www.transparenttextures.com/patterns/carbon-fibre.png');
        background-attachment: fixed;
    }
    
    /* Title Margin Box */
    .title-box {
        border: 3px solid #4a90e2;
        padding: 20px;
        margin: 10px auto;
        border-radius: 15px;
        text-align: center;
        background: rgba(74, 144, 226, 0.05);
    }
    .main-title {
        color: #4a90e2;
        font-size: 40px;
        font-weight: 800;
        text-transform: uppercase;
        margin: 0;
    }

    /* Created By & Roll Number */
    .user-info-bar {
        background: rgba(255, 255, 255, 0.03);
        border-bottom: 2px solid #d4af37;
        padding: 8px 20px;
        width: fit-content;
        margin: 0 auto 30px auto;
        text-align: center;
    }
    .user-info-text {
        color: #d4af37;
        font-size: 17px;
        font-family: 'Courier New', monospace;
        margin: 0;
    }

    /* Turbine Animation CSS */
    @keyframes rotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    .turbine-container {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 20px;
        background: #1e2130;
        border-radius: 50%;
        width: 100px;
        height: 100px;
        margin: 10px auto;
        border: 4px solid #3d4256;
    }
    .turbine-blade {
        font-size: 60px;
        animation: rotate 2s linear infinite;
        color: #d4af37;
    }

    /* Steam Animation for Button */
    @keyframes steam {
        0% { transform: translateY(0) scale(1); opacity: 0; }
        50% { opacity: 0.4; }
        100% { transform: translateY(-120px) scale(2.5); opacity: 0; }
    }
    .steam-effect {
        position: absolute;
        width: 25px;
        height: 25px;
        background: rgba(255, 255, 255, 0.2);
        border-radius: 50%;
        filter: blur(8px);
        animation: steam 1.5s infinite;
    }
    
    .stButton>button {
        background: radial-gradient(circle, #ff4b4b 0%, #a50000 100%);
        color: white;
        border-radius: 50%;
        width: 140px;
        height: 140px;
        border: 4px solid #2c303d;
        font-weight: bold;
        margin: 20px auto;
        display: block;
        position: relative;
        z-index: 5;
    }
    </style>
    """, unsafe_allow_html=True)

# 1. Main Heading inside Margin Box
st.markdown('<div class="title-box"><h1 class="main-title">Thermodynamics Property Finder</h1></div>', unsafe_allow_html=True)

# 2. Profile Section
st.markdown('<div class="user-info-bar"><p class="user-info-text">Created by: Ramish Ali | Roll Number: 25-ME-87</p></div>', unsafe_allow_html=True)

# 3. Sidebar with Live Turbine Animation
st.sidebar.title("Industrial Dashboard")
st.sidebar.write("Core Status: **Stable**")

# Turbine Animation in Sidebar
st.sidebar.markdown("""
    <div class="turbine-container">
        <div class="turbine-blade">⚙️</div>
    </div>
    <p style="text-align: center; color: #d4af37;">Live Turbine Operation</p>
    """, unsafe_allow_html=True)

st.sidebar.progress(100)
st.sidebar.info("RPM: 3500 | System Optimal")

# 4. Content Layout
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("### 📥 Input Data")
    R = st.number_input("Gas Constant R (J/kg-K)", value=287.0)
    T = st.number_input("Temperature (K)", value=300.0)
    P = st.number_input("Pressure (Pa)", value=101325.0)
    
    st.write("##")
    calculate = st.button("CALCULATE")
    
    if calculate:
        for i in range(5):
            st.markdown(f'<div class="steam-effect" style="left:{45+i*2}%; animation-delay:{i*0.3}s;"></div>', unsafe_allow_html=True)

with col2:
    st.markdown("### 📊 Live P-V Analysis")
    v = np.linspace(0.1, 1.2, 100)
    p = (R * T) / v
    chart_data = pd.DataFrame({'Vol': v, 'Pres': p})
    st.line_chart(chart_data.set_index('Vol'))

# 5. Results
if calculate:
    with st.spinner('Calculating...'):
        time.sleep(0.8)
    density = P / (R * T)
    spec_vol = 1 / density
    st.divider()
    res_a, res_b = st.columns(2)
    res_a.metric("Fluid Density (ρ)", f"{density:.4f} kg/m³")
    res_b.metric("Specific Volume (v)", f"{spec_vol:.4f} m³/kg")
