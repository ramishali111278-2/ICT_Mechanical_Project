import streamlit as st
import numpy as np
import pandas as pd

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

    /* Main Container with Partition */
    .main-box {
        border: 2px solid #4a90e2;
        border-radius: 15px;
        background: rgba(15, 18, 25, 0.8);
        box-shadow: 0 0 20px rgba(74, 144, 226, 0.3);
        padding: 20px;
        margin-top: 20px;
    }

    /* Vertical Divider Style */
    .vertical-line {
        border-left: 2px solid rgba(74, 144, 226, 0.5);
        height: 400px;
        position: absolute;
        left: 50%;
        top: 10%;
    }

    /* Bold Result Styling */
    .result-text {
        font-weight: 900 !important;
        font-size: 20px !important;
        color: #ffffff !important;
        background-color: #28a745;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        border: 2px solid #1e7e34;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }

    /* Turbine Animation */
    .turbine-container { text-align: center; padding: 10px; }
    .turbine-blade { font-size: 50px; animation: rotate 2s linear infinite; display: inline-block; color: #d4af37; }
    @keyframes rotate { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }

    /* Red Calculate Button */
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
        margin-top: 10px;
    }
    
    .title-box {
        border: 2px solid #4a90e2;
        padding: 10px;
        border-radius: 12px;
        text-align: center;
        background: rgba(74, 144, 226, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Header
st.markdown('<div class="title-box"><h1 style="color:#4a90e2; margin:0;">Thermodynamics Property Finder</h1></div>', unsafe_allow_html=True)
st.write(f"<p style='text-align:center; color:#d4af37; font-weight:bold;'>Created by: Ramish Ali | Reg. No: 25-ME-87</p>", unsafe_allow_html=True)

# 4. Sidebar
st.sidebar.title("Industrial Dashboard")
st.sidebar.markdown('<div class="turbine-container"><div class="turbine-blade">⚙️</div><p style="color:#d4af37; font-weight:bold;">TURBINE ACTIVE</p></div>', unsafe_allow_html=True)
st.sidebar.info("Core Status: Stable")

# 5. Main UI with Columns and Partition
st.markdown('<div class="main-box">', unsafe_allow_html=True)
col1, mid, col2 = st.columns([1, 0.1, 1])

with col1:
    st.markdown("### 📥 Input Parameters")
    gas_r = st.number_input("Gas Constant R (J/kg-K)", value=287.0, key="r")
    temp = st.number_input("Temperature (K)", value=300.0, key="t")
    pres = st.number_input("Pressure (Pa)", value=101325.0, key="p")
    st.write("##")
    calculate = st.button("CALCULATE")

with mid:
    # Vertical Partition Line
    st.markdown('<div class="vertical-line"></div>', unsafe_allow_html=True)

with col2:
    st.markdown("### 📊 P-V Diagram Analysis")
    v = np.linspace(0.1, 1.0, 50)
    p = (gas_r * temp) / v
    chart_data = pd.DataFrame({'Volume': v, 'Pressure': p}).set_index('Volume')
    st.line_chart(chart_data, use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# 6. Results - Bold and Styled
if calculate:
    density = pres / (gas_r * temp)
    st.write("##")
    # Yahan result ko bold aur bada dikhane ke liye kustom HTML use kiya gaya hai
    result_html = f"""
    <div class="result-text">
        ANALYSIS COMPLETE! FLUID DENSITY: {density:.4f} kg/m³
    </div>
    """
    st.markdown(result_html, unsafe_allow_html=True)
