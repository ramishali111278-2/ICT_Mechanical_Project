import streamlit as st
import numpy as np
import pandas as pd
import time

# 1. Page Configuration
st.set_page_config(page_title="Thermodynamics Property Finder", layout="wide")

# 2. Advanced CSS - Fixing the layout and removing empty boxes
st.markdown("""
    <style>
    /* Background */
    .stApp {
        background-color: #0a0c10;
        background-image: linear-gradient(rgba(10, 12, 16, 0.8), rgba(10, 12, 16, 0.8)),
            url('https://www.transparenttextures.com/patterns/carbon-fibre.png');
    }

    /* Main Container (Removing the extra blue empty box) */
    .content-wrapper {
        border: 2px solid #4a90e2;
        border-radius: 15px;
        background: rgba(15, 18, 25, 0.85);
        box-shadow: 0 0 25px rgba(74, 144, 226, 0.3);
        padding: 30px;
        margin-top: 10px;
    }

    /* Vertical Partition Line Fix */
    .v-line {
        border-left: 2px solid rgba(74, 144, 226, 0.5);
        height: 450px;
        margin: auto;
    }

    /* Bold Result Box */
    .result-text {
        font-weight: 900 !important;
        font-size: 22px !important;
        color: white !important;
        background-color: #28a745;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        border: 2px solid #1e7e34;
        margin-top: 20px;
    }

    /* Lightning Flash Effect */
    @keyframes lightning-strike {
        0% { width: 0%; opacity: 0; left: 50%; }
        20% { width: 100%; opacity: 1; left: 0%; box-shadow: 0 0 25px #00f0ff; }
        100% { width: 100%; opacity: 0; left: 0%; }
    }
    .lightning-flash {
        height: 5px;
        background: white;
        animation: lightning-strike 0.5s ease-out forwards;
        margin: 15px 0;
    }

    /* Red Calculate Button */
    .stButton > button {
        background: radial-gradient(circle, #ff4b4b 0%, #a50000 100%) !important;
        color: white !important;
        width: 100% !important;
        height: 55px !important;
        font-weight: bold !important;
        font-size: 18px !important;
        border-radius: 8px !important;
        text-transform: uppercase;
        border: 2px solid #111 !important;
    }

    .turbine-blade { font-size: 50px; animation: rotate 2s linear infinite; display: inline-block; color: #d4af37; }
    @keyframes rotate { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    </style>
    """, unsafe_allow_html=True)

# 3. Header Section
st.markdown('<div style="border: 2px solid #4a90e2; padding: 15px; border-radius: 12px; text-align: center; background: rgba(74, 144, 226, 0.1);"> <h1 style="color:#4a90e2; margin:0;">Thermodynamics Property Finder</h1></div>', unsafe_allow_html=True)
st.write(f"<p style='text-align:center; color:#d4af37; font-weight:bold; font-size:16px; margin-top:5px;'>Created by: Ramish Ali | Reg. No: 25-ME-87</p>", unsafe_allow_html=True)

# 4. Sidebar
st.sidebar.title("Industrial Dashboard")
st.sidebar.markdown('<div style="text-align:center; margin-top:20px;"><div class="turbine-blade">⚙️</div><p style="color:#d4af37; font-weight:bold;">TURBINE ACTIVE</p></div>', unsafe_allow_html=True)

# 5. Main UI (Combined Box with Partition)
st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

col1, divider, col2 = st.columns([1, 0.05, 1])

with col1:
    st.markdown("### 📥 Input Parameters")
    r_val = st.number_input("Gas Constant R (J/kg-K)", value=287.0)
    t_val = st.number_input("Temperature (K)", value=300.0)
    p_val = st.number_input("Pressure (Pa)", value=101325.0)
    st.write("##")
    calc_btn = st.button("CALCULATE")
    flash_placeholder = st.empty()

with divider:
    # Drawing the Vertical Line
    st.markdown('<div class="v-line"></div>', unsafe_allow_html=True)

with col2:
    st.markdown("### 📊 P-V Diagram Analysis")
    vol = np.linspace(0.1, 1.0, 50)
    pres = (r_val * t_val) / vol
    data = pd.DataFrame({'Volume': vol, 'Pressure': pres}).set_index('Volume')
    st.line_chart(data, use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# 6. Results Logic
if calc_btn:
    flash_placeholder.markdown('<div class="lightning-flash"></div>', unsafe_allow_html=True)
    time.sleep(0.2)
    
    rho = p_val / (r_val * t_val)
    st.markdown(f"""
        <div class="result-text">
            ANALYSIS COMPLETE! FLUID DENSITY: {rho:.4f} kg/m³
        </div>
    """, unsafe_allow_html=True)
