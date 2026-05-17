import streamlit as st
import numpy as np
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="Thermodynamics Property Finder", layout="wide")

# 2. Custom CSS for Industrial UI (Animations and Sound logic removed)
st.markdown("""
    <style>
    .stApp {
        background-color: #11141b;
        background-image: linear-gradient(rgba(17, 20, 27, 0.9), rgba(17, 20, 27, 0.9)),
            url('https://www.transparenttextures.com/patterns/carbon-fibre.png');
        background-attachment: fixed;
    }
    .title-box {
        border: 3px solid #4a90e2;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        background: rgba(74, 144, 226, 0.05);
        margin-bottom: 10px;
    }
    .main-title { color: #4a90e2; font-size: 40px; font-weight: 800; text-transform: uppercase; margin: 0; }
    
    /* Turbine UI */
    .turbine-system { position: relative; height: 120px; display: flex; align-items: center; justify-content: center; }
    .pipe { height: 12px; width: 50px; background: linear-gradient(to bottom, #555, #222); border: 1px solid #777; }
    .turbine-housing { width: 80px; height: 80px; background: #1e2130; border: 4px solid #3d4256; border-radius: 50%; display: flex; justify-content: center; align-items: center; }
    @keyframes rotate { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    .turbine-blade { font-size: 45px; animation: rotate 1.5s linear infinite; color: #d4af37; }

    /* Red Action Button */
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
        transition: 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        border-color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Header Section
st.markdown('<div class="title-box"><h1 class="main-title">Thermodynamics Property Finder</h1></div>', unsafe_allow_html=True)
st.markdown('<div style="text-align:center; color:#d4af37; margin-bottom:30px; font-family: sans-serif;">Created by: Ramish Ali | Roll Number: 25-ME-87</div>', unsafe_allow_html=True)

# 4. Sidebar Dashboard
st.sidebar.title("Industrial Dashboard")
st.sidebar.write("Core Status: **Stable**")
st.sidebar.markdown("""
    <div class="turbine-system">
        <div class="pipe" style="border-radius: 5px 0 0 5px;"></div>
        <div class="turbine-housing"><div class="turbine-blade">⚙️</div></div>
        <div class="pipe" style="border-radius: 0 5px 5px 0;"></div>
    </div>
    <p style="text-align: center; color: #d4af37; padding-top: 10px;">System Online</p>
    """, unsafe_allow_html=True)

# 5. Main Content Layout
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("### 📥 Input Data")
    R = st.number_input("Gas Constant R (J/kg-K)", value=287.0)
    T = st.number_input("Temperature (K)", value=300.0)
    P = st.number_input("Pressure (Pa)", value=101325.0)
    
    st.write("##") # Spacing
    calculate = st.button("CALCULATE")

with col2:
    st.markdown("### 📊 Live P-V Analysis")
    # Generating curve based on input
    v_range = np.linspace(0.1, 1.2, 100)
    p_range = (R * T) / v_range
    chart_data = pd.DataFrame({'Vol': v_range, 'Pres': p_range})
    st.line_chart(chart_data.set_index('Vol'))

# 6. Results Logic (No sound triggering here)
if calculate:
    density = P / (R * T)
    spec_vol = 1 / density
    
    st.divider()
    res_col1, res_col2 = st.columns(2)
    
    with res_col1:
        st.metric("Fluid Density (ρ)", f"{density:.4f} kg/m³")
    with res_col2:
        st.metric("Specific Volume (v)", f"{spec_vol:.4f} m³/kg")
        
    st.success("Analysis Complete. No errors detected.")
