import streamlit as st
import numpy as np
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="Thermodynamics Property Finder", layout="wide")

# 2. Advanced CSS - Fixing the layout issues
st.markdown("""
    <style>
    /* Background Fix */
    .stApp {
        background-color: #0a0c10;
        background-image: linear-gradient(rgba(10, 12, 16, 0.8), rgba(10, 12, 16, 0.8)),
            url('https://www.transparenttextures.com/patterns/carbon-fibre.png');
    }

    /* Lightning Box Styling */
    [data-testid="stVerticalBlock"] > div:has(div.lightning-container) {
        border: 2px solid #4a90e2;
        padding: 20px;
        border-radius: 15px;
        background: rgba(15, 18, 25, 0.7);
        box-shadow: 0 0 15px rgba(74, 144, 226, 0.3);
        margin-bottom: 20px;
    }

    /* Animation for the top of the box */
    .box-header {
        height: 3px;
        width: 100%;
        background: linear-gradient(90deg, transparent, #00f0ff, #0072ff, transparent);
        margin-bottom: 15px;
        animation: neon-glow 2s linear infinite;
    }

    @keyframes neon-glow {
        0% { background-position: -200% 0; }
        100% { background-position: 200% 0; }
    }

    /* Turbine CSS Fix */
    .turbine-container { text-align: center; padding: 10px; }
    .turbine-blade { font-size: 50px; animation: rotate 2s linear infinite; display: inline-block; color: #d4af37; }
    @keyframes rotate { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }

    /* Centered Red Button */
    .stButton > button {
        background: radial-gradient(circle, #ff4b4b 0%, #a50000 100%) !important;
        color: white !important;
        border-radius: 50% !important;
        width: 110px !important;
        height: 110px !important;
        font-weight: bold !important;
        border: 3px solid #222 !important;
        display: block;
        margin: 0 auto;
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
st.write(f"<p style='text-align:center; color:#d4af37; font-weight:bold; margin-top:5px;'>Created by: Ramish Ali | Reg. No: 25-ME-87</p>", unsafe_allow_html=True)

# 4. Sidebar (Dashboard setting fix)
st.sidebar.title("Industrial Dashboard")
st.sidebar.markdown('<div class="turbine-container"><div class="turbine-blade">⚙️</div><p style="color:#d4af37; font-weight:bold;">TURBINE ACTIVE</p></div>', unsafe_allow_html=True)
st.sidebar.info("System Status: Stable")

# 5. Main UI
col1, col2 = st.columns(2, gap="medium")

with col1:
    # Div dummy to trigger the CSS selector
    st.markdown('<div class="lightning-container"></div><div class="box-header"></div>', unsafe_allow_html=True)
    st.markdown("### 📥 Input Parameters")
    
    gas_r = st.number_input("Gas Constant R (J/kg-K)", value=287.0)
    temp = st.number_input("Temperature (K)", value=300.0)
    pres = st.number_input("Pressure (Pa)", value=101325.0)
    
    st.write("##")
    calculate = st.button("CALC")

with col2:
    # Div dummy to trigger the CSS selector
    st.markdown('<div class="lightning-container"></div><div class="box-header"></div>', unsafe_allow_html=True)
    st.markdown("### 📊 P-V Diagram Analysis")
    
    v = np.linspace(0.1, 1.0, 50)
    p = (gas_r * temp) / v
    chart_data = pd.DataFrame({'Volume': v, 'Pressure': p}).set_index('Volume')
    st.line_chart(chart_data, use_container_width=True)

# 6. Results
if calculate:
    density = pres / (gas_r * temp)
    st.divider()
    st.success(f"Analysis Complete! Fluid Density: **{density:.4f} kg/m³**")
