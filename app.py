import streamlit as st
import numpy as np
import pandas as pd
import time

# 1. Page Configuration
st.set_page_config(page_title="Thermodynamics Property Finder", layout="wide")

# 2. Advanced CSS for Horizontal Lightning and Storm
st.markdown("""
    <style>
    .stApp {
        background-color: #0a0c10;
        background-image: linear-gradient(rgba(10, 12, 16, 0.8), rgba(10, 12, 16, 0.8)),
            url('https://www.transparenttextures.com/patterns/carbon-fibre.png');
    }

    /* Lightning Flash Effect on Background */
    @keyframes lightning-flash {
        0% { background-color: #0a0c10; }
        10% { background-color: #2c3e50; }
        15% { background-color: #0a0c10; }
        20% { background-color: #4a90e2; }
        25% { background-color: #0a0c10; }
    }

    /* Horizontal Lightning Bolt Animation */
    @keyframes horizontal-bolt {
        0% { transform: scaleX(0); opacity: 0; }
        50% { transform: scaleX(1); opacity: 1; }
        100% { transform: scaleX(0); opacity: 0; }
    }

    .lightning-horizontal {
        position: relative;
        width: 100%;
        height: 8px;
        background: white;
        box-shadow: 0 0 20px 8px #4a90e2, 0 0 40px 15px #ffffff;
        margin-top: -20px; /* Positioned right below the button */
        z-index: 10;
        border-radius: 4px;
        animation: horizontal-bolt 0.4s ease-in-out forwards;
    }

    /* UI Styling */
    .title-box {
        border: 2px solid #4a90e2;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        background: rgba(74, 144, 226, 0.1);
        margin-bottom: 20px;
    }
    
    .turbine-blade {
        font-size: 50px;
        display: inline-block;
        animation: rotate 2s linear infinite;
        color: #d4af37;
    }
    @keyframes rotate { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }

    /* Red Industrial Button */
    .stButton>button {
        background: radial-gradient(circle, #ff4b4b 0%, #a50000 100%);
        color: white;
        border-radius: 50%;
        width: 140px;
        height: 140px;
        font-weight: bold;
        border: 4px solid #1e2130;
        z-index: 20;
        position: relative;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Heading & Student Info
st.markdown('<div class="title-box"><h1 style="color:#4a90e2; margin:0;">Thermodynamics Property Finder</h1></div>', unsafe_allow_html=True)
st.write(f"<p style='text-align:center; color:#d4af37; font-size:14px;'>User: Ramish Ali | ID: 25-ME-87</p>", unsafe_allow_html=True)

# 4. Sidebar Layout
st.sidebar.title("Control Panel")
st.sidebar.markdown('<div style="text-align:center;"><span class="turbine-blade">⚙️</span></div>', unsafe_allow_html=True)
st.sidebar.info("Core Status: Stable")

# 5. Main UI Columns
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("### 📥 Input Parameters")
    R = st.number_input("Gas Constant R (J/kg-K)", value=287.0)
    T = st.number_input("Temperature (K)", value=300.0)
    P = st.number_input("Pressure (Pa)", value=101325.0)
    
    st.write("##") # Spacing for the button
    calculate = st.button("CALCULATE")
    
    # Check if button is pressed to show horizontal lightning
    if calculate:
        st.markdown('<div class="lightning-horizontal"></div>', unsafe_allow_html=True)

with col2:
    st.markdown("### 📊 P-V Diagram Analysis")
    v = np.linspace(0.1, 1.0, 50)
    p = (R * T) / v
    st.line_chart(pd.DataFrame({'Volume': v, 'Pressure': p}).set_index('Volume'))

# 6. Results Logic
if calculate:
    # Trigger background flash
    st.markdown('<style>.stApp { animation: lightning-flash 0.5s ease-out; }</style>', unsafe_allow_html=True)
    
    density = P / (R * T)
    st.divider()
    st.metric("Fluid Density (ρ)", f"{density:.4f} kg/m³")
    st.success("Lightning Analysis Complete: Horizontal Strike Detected!")
