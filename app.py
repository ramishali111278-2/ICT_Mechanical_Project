import streamlit as st
import numpy as np
import pandas as pd
import time

# Page configuration
st.set_page_config(page_title="Thermodynamics Property Finder", layout="wide")

# Custom CSS for New Layout and Industrial Theme
st.markdown("""
    <style>
    /* Industrial Background with specialized texture */
    .stApp {
        background-color: #11141b;
        background-image: 
            linear-gradient(rgba(17, 20, 27, 0.9), rgba(17, 20, 27, 0.9)),
            url('https://www.transparenttextures.com/patterns/carbon-fibre.png');
        background-attachment: fixed;
    }
    
    /* Top Main Heading */
    .main-title {
        text-align: center;
        color: #4a90e2;
        font-size: 45px;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-top: -30px;
        text-shadow: 2px 2px 10px rgba(74, 144, 226, 0.3);
    }

    /* Profile Section (Below Heading) */
    .user-info-bar {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(212, 175, 55, 0.3);
        border-radius: 10px;
        padding: 10px 20px;
        width: fit-content;
        margin: 10px auto 30px auto;
        text-align: center;
    }
    .user-info-text {
        color: #d4af37;
        font-size: 18px;
        font-family: 'Courier New', monospace;
        margin: 0;
    }

    /* Industrial Circular Button with Steam Effect */
    .stButton>button {
        background: radial-gradient(circle, #ff4b4b 0%, #a50000 100%);
        color: white;
        border-radius: 50%;
        width: 140px;
        height: 140px;
        border: 4px solid #2c303d;
        font-weight: bold;
        font-size: 18px;
        margin: 20px auto;
        display: block;
        transition: 0.3s;
        position: relative;
        z-index: 5;
    }
    
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
    </style>
    """, unsafe_allow_html=True)

# 1. Main Heading (Top)
st.markdown('<h1 class="main-title">Thermodynamics Property Finder</h1>', unsafe_allow_html=True)

# 2. Profile Section (Below Heading)
st.markdown("""
    <div class="user-info-bar">
        <p class="user-info-text">User: Ramish Ali | ID: 25-ME-87</p>
    </div>
    """, unsafe_allow_html=True)

# 3. Content Layout
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("### ⚙️ Engine Parameters")
    R = st.number_input("Gas Constant R (J/kg-K)", value=287.0)
    T = st.number_input("Temperature (K)", value=300.0)
    P = st.number_input("Pressure (Pa)", value=101325.0)
    
    st.write("##")
    # Circular Button
    calculate = st.button("CALCULATE")
    
    if calculate:
        # Steam/Smoke particles
        for i in range(5):
            st.markdown(f'<div class="steam-effect" style="left:{45+i*2}%; animation-delay:{i*0.3}s;"></div>', unsafe_allow_html=True)

with col2:
    st.markdown("### 📊 Live P-V Analysis")
    v = np.linspace(0.1, 1.2, 100)
    p = (R * T) / v
    chart_data = pd.DataFrame({'Vol': v, 'Pres': p})
    st.line_chart(chart_data.set_index('Vol'))

# 4. Processing and Results
if calculate:
    with st.spinner('Processing Steam Cycle...'):
        time.sleep(0.8) # Wait for animation
    
    density = P / (R * T)
    spec_vol = 1 / density
    
    st.divider()
    res_a, res_b = st.columns(2)
    res_a.metric("Fluid Density (ρ)", f"{density:.4f} kg/m³")
    res_b.metric("Specific Volume (v)", f"{spec_vol:.4f} m³/kg")
    st.success("Analysis Complete.")

# Sidebar for Industrial Gadgets
st.sidebar.title("Industrial Dashboard")
st.sidebar.markdown("---")
st.sidebar.write("Core Status: **Stable**")
st.sidebar.progress(100)
st.sidebar.info("Sensor 01 Calibration: OK")
