import streamlit as st
import numpy as np
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="Thermodynamics Property Finder", layout="wide")

# 2. Advanced CSS for Lightning Borders and Animations
st.markdown("""
    <style>
    .stApp {
        background-color: #0a0c10;
        background-image: linear-gradient(rgba(10, 12, 16, 0.8), rgba(10, 12, 16, 0.8)),
            url('https://www.transparenttextures.com/patterns/carbon-fibre.png');
    }

    /* Lightning Glowing Box Effect */
    .lightning-box {
        border: 2px solid #4a90e2;
        padding: 20px;
        border-radius: 15px;
        background: rgba(10, 12, 16, 0.6);
        box-shadow: 0 0 15px rgba(74, 144, 226, 0.4);
        position: relative;
        margin-bottom: 20px;
        min-height: 450px; /* باکس کی اونچائی کو برابر رکھنے کے لیے */
    }
    
    /* Neon Top Border Animation Line */
    .lightning-box::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 3px;
        background: linear-gradient(90deg, transparent, #00f0ff, #0072ff, transparent);
        animation: neon-glow 2s linear infinite;
    }

    @keyframes neon-glow {
        0% { background-position: -200% 0; }
        100% { background-position: 200% 0; }
    }

    /* Turbine and Steam Animations */
    .turbine-container { display: flex; align-items: center; justify-content: center; padding: 20px 0; }
    .turbine-housing { width: 70px; height: 70px; background: #1e2130; border: 4px solid #3d4256; border-radius: 50%; display: flex; justify-content: center; align-items: center; }
    .turbine-blade { font-size: 40px; animation: rotate 2s linear infinite; color: #d4af37; }
    @keyframes rotate { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    
    .title-box { border: 2px solid #4a90e2; padding: 15px; border-radius: 12px; text-align: center; background: rgba(74, 144, 226, 0.1); margin-bottom: 20px; }
    
    /* Styled Round Button */
    .stButton>button {
        background: radial-gradient(circle, #ff4b4b 0%, #a50000 100%) !important;
        color: white !important;
        border-radius: 50% !important;
        width: 100px !important;
        height: 100px !important;
        font-weight: bold !important;
        border: 3px solid #1e2130 !important;
        box-shadow: 0 0 15px rgba(255, 75, 75, 0.4) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Header
st.markdown('<div class="title-box"><h1 style="color:#4a90e2; margin:0;">Thermodynamics Property Finder</h1></div>', unsafe_allow_html=True)
st.write(f"<p style='text-align:center; color:#d4af37; font-size:15px; font-weight:bold;'>Created by: Ramish Ali | Reg. No: 25-ME-87</p>", unsafe_allow_html=True)

# 4. Sidebar
st.sidebar.title("Industrial Dashboard")
st.sidebar.markdown("""<div class="turbine-container"><div class="turbine-housing"><div class="turbine-blade">⚙️</div></div></div>""", unsafe_allow_html=True)

# 5. Main UI
col1, col2 = st.columns(2)

with col1:
    # ان پٹ پیرامیٹرز کو باکس کے اندر ڈالنے کے لیے HTML کو اوپر اور نیچے "wrap" کیا گیا ہے
    st.markdown('<div class="lightning-box">', unsafe_allow_html=True)
    st.markdown("### 📥 Input Parameters")
    
    gas_r = st.number_input("Gas Constant R (J/kg-K)", value=287.0)
    temp = st.number_input("Temperature (K)", value=300.0)
    pres = st.number_input("Pressure (Pa)", value=101325.0)
    
    st.write("##")
    calculate = st.button("CALC")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    # گراف کو باکس کے اندر ڈالنے کے لیے HTML کو "wrap" کیا گیا ہے
    st.markdown('<div class="lightning-box">', unsafe_allow_html=True)
    st.markdown("### 📊 P-V Diagram Analysis")
    
    v = np.linspace(0.1, 1.0, 50)
    p = (gas_r * temp) / v
    chart_data = pd.DataFrame({'Volume': v, 'Pressure': p}).set_index('Volume')
    st.line_chart(chart_data)
    st.markdown('</div>', unsafe_allow_html=True)

# 6. Results
if calculate:
    density = pres / (gas_r * temp)
    st.success(f"Calculation Complete! Fluid Density: {density:.4f} kg/m³")
