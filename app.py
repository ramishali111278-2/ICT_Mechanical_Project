import streamlit as st
import numpy as np
import pandas as pd
import time
import base64

# Page configuration
st.set_page_config(page_title="Thermodynamics Property Finder", layout="wide")

# --- Function to play sound via Base64 ---
def play_steam_sound(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            md = f"""
                <audio autoplay="true">
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
                """
            st.markdown(md, unsafe_allow_html=True)
    except Exception as e:
        # Agar file nahi milti toh error sidebar mein show hoga debugging ke liye
        st.sidebar.error(f"Sound Error: {e}")

# Custom CSS for Industrial UI and Turbine
st.markdown("""
    <style>
    .stApp {
        background-color: #11141b;
        background-image: linear-gradient(rgba(17, 20, 27, 0.9), rgba(17, 20, 27, 0.9)),
            url('https://www.transparenttextures.com/patterns/carbon-fibre.png');
        background-attachment: fixed;
    }
    
    /* Heading Box */
    .title-box {
        border: 3px solid #4a90e2;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        background: rgba(74, 144, 226, 0.05);
        margin-bottom: 10px;
    }
    .main-title { color: #4a90e2; font-size: 40px; font-weight: 800; text-transform: uppercase; margin: 0; }
    
    /* Turbine and Pipes */
    .turbine-system { position: relative; height: 150px; display: flex; align-items: center; justify-content: center; }
    .pipe { height: 15px; width: 60px; background: linear-gradient(to bottom, #555, #222); border: 1px solid #777; }
    .turbine-housing { width: 90px; height: 90px; background: #1e2130; border: 4px solid #3d4256; border-radius: 50%; display: flex; justify-content: center; align-items: center; z-index: 2; }
    @keyframes rotate { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    .turbine-blade { font-size: 50px; animation: rotate 1.5s linear infinite; color: #d4af37; }

    /* Red Industrial Button (No Animation) */
    .stButton>button {
        background: radial-gradient(circle, #ff4b4b 0%, #a50000 100%);
        color: white;
        border-radius: 50%;
        width: 140px;
        height: 140px;
        border: 4px solid #2c303d;
        font-weight: bold;
        display: block;
        margin: 20px auto;
        font-size: 16px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.03);
        border-color: #ffffff;
    }
    </style>
    """, unsafe_allow_html=True)

# 1. Title Section
st.markdown('<div class="title-box"><h1 class="main-title">Thermodynamics Property Finder</h1></div>', unsafe_allow_html=True)
st.markdown('<div style="text-align:center; color:#d4af37; margin-bottom:30px; font-family:monospace;">Created by: Ramish Ali | Roll Number: 25-ME-87</div>', unsafe_allow_html=True)

# 2. Sidebar Layout
st.sidebar.title("Industrial Dashboard")
st.sidebar.write("Core Status: **Stable**")
st.sidebar.markdown("""
    <div class="turbine-system">
        <div class="pipe" style="border-radius: 5px 0 0 5px;"></div>
        <div class="turbine-housing"><div class="turbine-blade">⚙️</div></div>
        <div class="pipe" style="border-radius: 0 5px 5px 0;"></div>
    </div>
    <p style="text-align: center; color: #d4af37; font-size: 14px;">Live Turbine Operation</p>
    """, unsafe_allow_html=True)
st.sidebar.progress(100)

# 3. Main Calculator UI
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("### 📥 Input Data")
    R = st.number_input("Gas Constant R (J/kg-K)", value=287.0)
    T = st.number_input("Temperature (K)", value=300.0)
    P = st.number_input("Pressure (Pa)", value=101325.0)
    
    st.write("##")
    calculate = st.button("CALCULATE")

with col2:
    st.markdown("### 📊 Live P-V Analysis")
    v = np.linspace(0.1, 1.2, 100)
    p = (R * T) / v
    st.line_chart(pd.DataFrame({'Vol': v, 'Pres': p}).set_index('Vol'))

# 4. Sound & Logic Execution
if calculate:
    # Sound play logic (Animation is now gone)
    play_steam_sound("steam.mp3")
    
    density = P / (R * T)
    spec_vol = 1 / density
    
    st.divider()
    res_a, res_b = st.columns(2)
    res_a.metric("Fluid Density (ρ)", f"{density:.4f} kg/m³")
    res_b.metric("Specific Volume (v)", f"{spec_vol:.4f} m³/kg")
    st.success("Analysis Complete.")
