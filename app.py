import streamlit as st
import numpy as np
import pandas as pd
import time

# Page configuration
st.set_page_config(page_title="Thermodynamics Property Finder", layout="wide")

# Custom CSS for Pipes, High Intensity Steam, and Turbine
st.markdown("""
    <style>
    /* Industrial Background */
    .stApp {
        background-color: #11141b;
        background-image: linear-gradient(rgba(17, 20, 27, 0.9), rgba(17, 20, 27, 0.9)),
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
    .main-title { color: #4a90e2; font-size: 40px; font-weight: 800; text-transform: uppercase; margin: 0; }

    /* Created By & Roll Number */
    .user-info-bar {
        background: rgba(255, 255, 255, 0.03);
        border-bottom: 2px solid #d4af37;
        padding: 8px 20px;
        width: fit-content;
        margin: 0 auto 30px auto;
        text-align: center;
    }
    .user-info-text { color: #d4af37; font-size: 17px; font-family: 'Courier New', monospace; margin: 0; }

    /* Turbine with Input/Output Pipes */
    .turbine-system {
        position: relative;
        height: 150px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .pipe {
        height: 15px;
        width: 60px;
        background: linear-gradient(to bottom, #555, #222);
        border: 1px solid #777;
    }
    .input-pipe { border-radius: 5px 0 0 5px; }
    .output-pipe { border-radius: 0 5px 5px 0; }
    
    .turbine-housing {
        width: 90px;
        height: 90px;
        background: #1e2130;
        border: 4px solid #3d4256;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 2;
    }
    @keyframes rotate { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    .turbine-blade { font-size: 50px; animation: rotate 1.5s linear infinite; color: #d4af37; }

    /* HIGH INTENSITY STEAM Animation */
    @keyframes steam-rise {
        0% { transform: translateY(0) scale(1); opacity: 0; }
        20% { opacity: 0.8; }
        100% { transform: translateY(-180px) scale(4); opacity: 0; }
    }
    .steam-heavy {
        position: absolute;
        width: 35px;
        height: 35px;
        background: rgba(255, 255, 255, 0.5); /* Zyada intensity */
        border-radius: 50%;
        filter: blur(12px);
        animation: steam-rise 1.2s infinite;
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
        z-index: 10;
    }
    </style>
    """, unsafe_allow_html=True)

# 1. Main Heading and Profile
st.markdown('<div class="title-box"><h1 class="main-title">Thermodynamics Property Finder</h1></div>', unsafe_allow_html=True)
st.markdown('<div class="user-info-bar"><p class="user-info-text">Created by: Ramish Ali | Roll Number: 25-ME-87</p></div>', unsafe_allow_html=True)

# 2. Sidebar with Turbine and Pipes
st.sidebar.title("Industrial Dashboard")
st.sidebar.write("Core Status: **Stable**")

st.sidebar.markdown("""
    <div class="turbine-system">
        <div class="pipe input-pipe"></div>
        <div class="turbine-housing">
            <div class="turbine-blade">⚙️</div>
        </div>
        <div class="pipe output-pipe"></div>
    </div>
    <p style="text-align: center; color: #d4af37; font-size: 14px;">Live Turbine Cycle (In/Out Pipes)</p>
    """, unsafe_allow_html=True)

st.sidebar.progress(100)
st.sidebar.info("System: Optimal Flow")

# 3. Content Layout
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("### 📥 Input Data")
    R = st.number_input("Gas Constant R (J/kg-K)", value=287.0)
    T = st.number_input("Temperature (K)", value=300.0)
    P = st.number_input("Pressure (Pa)", value=101325.0)
    
    st.write("##")
    calculate = st.button("CALCULATE")
    
    if calculate:
        # High Intensity Steam (More particles)
        for i in range(12): # Particles ki tadad barha di
            st.markdown(f'<div class="steam-heavy" style="left:{40+i*2}%; animation-delay:{i*0.1}s;"></div>', unsafe_allow_html=True)

with col2:
    st.markdown("### 📊 Live P-V Analysis")
    v = np.linspace(0.1, 1.2, 100)
    p = (R * T) / v
    chart_data = pd.DataFrame({'Vol': v, 'Pres': p})
    st.line_chart(chart_data.set_index('Vol'))

# 4. Results
if calculate:
    time.sleep(1.0) # Animation enjoy karne ke liye thoda wait
    density = P / (R * T)
    spec_vol = 1 / density
    st.divider()
    res_a, res_b = st.columns(2)
    res_a.metric("Fluid Density (ρ)", f"{density:.4f} kg/m³")
    res_b.metric("Specific Volume (v)", f"{spec_vol:.4f} m³/kg")
