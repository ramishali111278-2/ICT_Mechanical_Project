import streamlit as st
import numpy as np
import pandas as pd
import time

# 1. Page Configuration
st.set_page_config(page_title="Thermodynamics Property Finder", layout="wide")

# 2. Advanced CSS
st.markdown("""
    <style>
    /* Background */
    .stApp {
        background-color: #0a0c10;
        background-image: linear-gradient(rgba(10, 12, 16, 0.8), rgba(10, 12, 16, 0.8)),
            url('https://www.transparenttextures.com/patterns/carbon-fibre.png');
    }

    /* Main Container without the extra empty box */
    .main-box {
        border: 2px solid #4a90e2;
        border-radius: 15px;
        background: rgba(15, 18, 25, 0.8);
        box-shadow: 0 0 20px rgba(74, 144, 226, 0.3);
        padding: 30px;
        margin-top: 10px;
        position: relative;
    }

    /* Vertical Partition Line - Precise Styling */
    .partition {
        border-left: 2px solid rgba(74, 144, 226, 0.5);
        height: 100%;
        position: absolute;
        left: 50%;
        top: 0;
    }

    /* Result Box Styling */
    .result-text {
        font-weight: 900 !important;
        font-size: 22px !important;
        color: #ffffff !important;
        background-color: #28a745;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        border: 2px solid #1e7e34;
        margin-top: 20px;
    }

    /* Lightning Flash Animation */
    @keyframes lightning-strike {
        0% { width: 0%; opacity: 0; left: 50%; }
        20% { width: 100%; opacity: 1; left: 0%; box-shadow: 0 0 20px #00f0ff; }
        100% { width: 100%; opacity: 0; left: 0%; }
    }
    .lightning-bolt {
        height: 4px;
        background: white;
        animation: lightning-strike 0.6s ease-out forwards;
        margin: 10px 0;
    }

    /* Button Styling */
    .stButton > button {
        background: radial-gradient(circle, #ff4b4b 0%, #a50000 100%) !important;
        color: white !important;
        width: 100% !important;
        height: 55px !important;
        font-weight: bold !important;
        font-size: 18px !important;
        border-radius: 8px !important;
        text-transform: uppercase;
    }

    .turbine-blade { font-size: 50px; animation: rotate 2s linear infinite; display: inline-block; color: #d4af37; }
    @keyframes rotate { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    </style>
    """, unsafe_allow_html=True)

# 3. Header Section
st.markdown('<div style="border: 2px solid #4a90e2; padding: 15px; border-radius: 12px; text-align: center; background: rgba(74, 144, 226, 0.1);"> <h1 style="color:#4a90e2; margin:0; font-family: sans-serif;">Thermodynamics Property Finder</h1></div>', unsafe_allow_html=True)
st.write(f"<p style='text-align:center; color:#d4af37; font-weight:bold; font-size:16px; margin-top:5px;'>Created by: Ramish Ali | Reg. No: 25-ME-87</p>", unsafe_allow_html=True)

# 4. Sidebar
st.sidebar.title("Industrial Dashboard")
st.sidebar.markdown('<div style="text-align:center; margin-top:20px;"><div class="turbine-blade">⚙️</div><p style="color:#d4af37; font-weight:bold; font-size:18px;">TURBINE ACTIVE</p></div>', unsafe_allow_html=True)

# 5. Main Content Area
st.markdown('<div class="main-box">', unsafe_allow_html=True)

# Columns setup
col1, space, col2 = st.columns([1, 0.1, 1])

with col1:
    st.markdown("### 📥 Input Parameters")
    gas_r = st.number_input("Gas Constant R (J/kg-K)", value=287.0)
    temp = st.number_input("Temperature (K)", value=300.0)
    pres = st.number_input("Pressure (Pa)", value=101325.0)
    st.write("##")
    calculate = st.button("CALCULATE")
    flash_holder = st.empty()

with space:
    # This creates the visual partition
    st.markdown('<div style="border-left: 2px solid rgba(74, 144, 226, 0.4); height: 400px; margin-left: 50%;"></div>', unsafe_allow_html=True)

with col2:
    st.markdown("### 📊 P-V Diagram Analysis")
    v_range = np.linspace(0.1, 1.0, 50)
    p_values = (gas_r * temp) / v_range
    chart_data = pd.DataFrame({'Volume': v_range, 'Pressure': p_values}).set_index('Volume')
    st.line_chart(chart_data, use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# 6. Logic and Output
if calculate:
    flash_holder.markdown('<div class="lightning-bolt"></div>', unsafe_allow_html=True)
    time.sleep(0.2)
    
    density = pres / (gas_r * temp)
    
    st.markdown(f"""
        <div class="result-text">
            ANALYSIS COMPLETE! FLUID DENSITY: {density:.4f} kg/m³
        </div>
    """, unsafe_allow_html=True)
