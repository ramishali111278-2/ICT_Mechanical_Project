import streamlit as st
import numpy as np
import pandas as pd
import time

# 1. Page Configuration (Must be the first Streamlit command)
st.set_page_config(page_title="Thermodynamics Property Finder", layout="wide")

# 2. Sound Function (Simplified to prevent Black Screen)
def play_steam_sound():
    sound_url = "https://www.soundjay.com/mechanical/sounds/steam-engine-inner-workings-1.mp3"
    # Hidden audio player that triggers on click
    st.markdown(f"""
        <audio autoplay>
            <source src="{sound_url}" type="audio/mp3">
        </audio>
    """, unsafe_allow_html=True)

# 3. Industrial CSS (Corrected to avoid rendering issues)
st.markdown("""
    <style>
    .stApp {
        background-color: #11141b;
        color: white;
    }
    .title-box {
        border: 2px solid #4a90e2;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        background: rgba(74, 144, 226, 0.1);
    }
    /* Turbine Animation */
    @keyframes rotate { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    .turbine-blade {
        font-size: 50px;
        display: inline-block;
        animation: rotate 2s linear infinite;
        color: #d4af37;
    }
    /* Big Red Button */
    .stButton>button {
        background-color: #ff4b4b !important;
        color: white !important;
        border-radius: 50% !important;
        width: 120px !important;
        height: 120px !important;
        font-weight: bold !important;
        border: 3px solid #2c303d !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- UI Layout ---
st.markdown('<div class="title-box"><h1>Thermodynamics Property Finder</h1></div>', unsafe_allow_html=True)
st.write(f"<p style='text-align:center;'>User: Ramish Ali | ID: 25-ME-87</p>", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Industrial Dashboard")
st.sidebar.markdown('<div style="text-align:center;"><span class="turbine-blade">⚙️</span></div>', unsafe_allow_html=True)
st.sidebar.info("Status: System Online")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📥 Input Data")
    R = st.number_input("Gas Constant R (J/kg-K)", value=287.0)
    T = st.number_input("Temperature (K)", value=300.0)
    P = st.number_input("Pressure (Pa)", value=101325.0)
    
    calculate = st.button("CALCULATE")

with col2:
    st.subheader("📊 P-V Diagram")
    v_vals = np.linspace(0.1, 1.0, 50)
    p_vals = (R * T) / v_vals
    df = pd.DataFrame({'Volume': v_vals, 'Pressure': p_vals})
    st.line_chart(df.set_index('Volume'))

# Result Logic
if calculate:
    play_steam_sound() # Sound trigger
    density = P / (R * T)
    st.success(f"Calculation Successful!")
    st.metric("Fluid Density (ρ)", f"{density:.4f} kg/m³")
