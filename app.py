import streamlit as st
import numpy as np
import pandas as pd
import time

# Page setup
st.set_page_config(page_title="Thermodynamics Property Finder", layout="wide")

# Custom CSS for Industrial Grid, Profile Header and STEAM Animation
st.markdown("""
    <style>
    /* Background with Industrial Grid */
    .stApp {
        background-color: #0e1117;
        background-image: radial-gradient(#2c303d 1px, transparent 1px);
        background-size: 30px 30px;
    }
    
    /* Header Section */
    .user-header {
        background: rgba(45, 49, 66, 0.8);
        border-left: 5px solid #d4af37;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 25px;
    }
    .user-name { color: #ffffff; font-size: 22px; font-weight: bold; margin: 0; }
    .user-roll { color: #d4af37; font-size: 18px; margin: 0; }

    /* Industrial Button */
    .stButton>button {
        background: radial-gradient(circle, #ff4b4b 0%, #a50000 100%);
        color: white;
        border-radius: 50%;
        width: 140px;
        height: 140px;
        border: 4px solid #3d4256;
        font-weight: bold;
        font-size: 18px;
        position: relative;
        z-index: 2;
        margin: 0 auto;
        display: block;
    }

    /* Smoke/Steam Animation Effect */
    @keyframes smoke {
        0% { transform: translateY(0) scale(1); opacity: 0; }
        50% { opacity: 0.5; }
        100% { transform: translateY(-150px) scale(3); opacity: 0; }
    }

    .steam-container {
        position: relative;
        width: 140px;
        margin: 0 auto;
    }

    .smoke-particle {
        position: absolute;
        top: 20px;
        left: 50%;
        width: 30px;
        height: 30px;
        background: rgba(200, 200, 200, 0.3);
        border-radius: 50%;
        filter: blur(10px);
        animation: smoke 2s infinite;
    }
    </style>
    """, unsafe_allow_html=True)

# 1. User Profile Section
st.markdown("""
    <div class="user-header">
        <p class="user-name">Name: Ramish Ali</p>
        <p class="user-roll">Roll Number: 25-ME-87</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #ffffff;'>Thermodynamics Property Finder</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("### 📥 Input Parameters")
    R = st.number_input("Gas Constant R (J/kg-K)", value=287.0)
    T = st.number_input("Temperature (K)", value=300.0)
    P = st.number_input("Pressure (Pa)", value=101325.0)
    
    st.write("##")
    
    # Calculate Button logic with animation trigger
    calculate = st.button("CALCULATE")
    
    if calculate:
        # Steam Animation HTML
        st.markdown("""
            <div class="steam-container">
                <div class="smoke-particle" style="animation-delay: 0.1s; left: 30%;"></div>
                <div class="smoke-particle" style="animation-delay: 0.5s; left: 50%;"></div>
                <div class="smoke-particle" style="animation-delay: 0.9s; left: 70%;"></div>
                <div class="smoke-particle" style="animation-delay: 1.3s; left: 40%;"></div>
            </div>
            """, unsafe_allow_html=True)

with col2:
    st.markdown("### 📈 P-V Diagram Analysis")
    v_range = np.linspace(0.1, 1.5, 100)
    p_range = (R * T) / v_range 
    df = pd.DataFrame({'Volume (m³)': v_range, 'Pressure (Pa)': p_range})
    st.line_chart(df.set_index('Volume (m³)'))

if calculate:
    # Dummy delay to show animation
    time.sleep(0.5)
    density = P / (R * T)
    spec_vol = 1 / density
    
    st.markdown("---")
    res1, res2 = st.columns(2)
    res1.metric("Density (ρ)", f"{density:.4f} kg/m³")
    res2.metric("Spec. Volume (v)", f"{spec_vol:.4f} m³/kg")

st.sidebar.title("🛠️ Control Panel")
st.sidebar.success("Engine Online 🟢")
st.sidebar.progress(100)
