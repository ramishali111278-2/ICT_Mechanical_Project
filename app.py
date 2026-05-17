import streamlit as st
import numpy as np
import pandas as pd
import time

# 1. Page Configuration
st.set_page_config(page_title="Thermodynamics Property Finder", layout="wide")

# 2. Advanced CSS for Lightning and Thunderstorm
st.markdown("""
    <style>
    .stApp {
        background-color: #0a0c10;
        background-image: linear-gradient(rgba(10, 12, 16, 0.8), rgba(10, 12, 16, 0.8)),
            url('https://www.transparenttextures.com/patterns/carbon-fibre.png');
        transition: background-color 0.1s;
    }

    /* Lightning Flash Effect */
    @keyframes lightning-flash {
        0% { background-color: #0a0c10; }
        10% { background-color: #4a90e2; }
        15% { background-color: #0a0c10; }
        20% { background-color: #ffffff; }
        25% { background-color: #0a0c10; }
        100% { background-color: #0a0c10; }
    }
    .storm-active {
        animation: lightning-flash 1s ease-out;
    }

    /* Thunder Bolt Animation */
    @keyframes bolt-strike {
        0% { opacity: 0; transform: scaleY(0); }
        50% { opacity: 1; transform: scaleY(1); }
        100% { opacity: 0; }
    }
    .lightning-bolt {
        position: fixed;
        top: 0;
        left: 50%;
        width: 5px;
        height: 100vh;
        background: white;
        box-shadow: 0 0 20px 5px #4a90e2;
        z-index: 9999;
        pointer-events: none;
        animation: bolt-strike 0.3s ease-in-out;
    }

    /* UI Styling */
    .title-box {
        border: 2px solid #4a90e2;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        background: rgba(74, 144, 226, 0.1);
    }
    .turbine-blade {
        font-size: 50px;
        display: inline-block;
        animation: rotate 2s linear infinite;
        color: #d4af37;
    }
    @keyframes rotate { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }

    .stButton>button {
        background: radial-gradient(circle, #ff4b4b 0%, #a50000 100%);
        color: white;
        border-radius: 50%;
        width: 130px;
        height: 130px;
        font-weight: bold;
        border: 4px solid #1e2130;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Heading
st.markdown('<div class="title-box"><h1 style="color:#4a90e2;">Thermodynamics Property Finder</h1></div>', unsafe_allow_html=True)
st.write(f"<p style='text-align:center; color:#d4af37;'>User: Ramish Ali | ID: 25-ME-87</p>", unsafe_allow_html=True)

# 4. Sidebar
st.sidebar.title("Control Panel")
st.sidebar.markdown('<div style="text-align:center;"><span class="turbine-blade">⚙️</span></div>', unsafe_allow_html=True)
st.sidebar.status("Core Status: Stable")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📥 Input Parameters")
    R = st.number_input("Gas Constant R (J/kg-K)", value=287.0)
    T = st.number_input("Temperature (K)", value=300.0)
    P = st.number_input("Pressure (Pa)", value=101325.0)
    calculate = st.button("CALCULATE")

with col2:
    st.markdown("### 📊 P-V Diagram Analysis")
    v = np.linspace(0.1, 1.0, 50)
    p = (R * T) / v
    st.line_chart(pd.DataFrame({'V': v, 'P': p}).set_index('V'))

# 5. Thunderstorm Logic
if calculate:
    # Adding lightning bolt and screen flash using HTML injection
    st.markdown('<div class="lightning-bolt"></div>', unsafe_allow_html=True)
    st.markdown('<style>.stApp { animation: lightning-flash 0.5s ease-out; }</style>', unsafe_allow_html=True)
    
    # Sound remove kar di gayi hai, sirf visual lightning aayegi
    density = P / (R * T)
    st.divider()
    st.metric("Fluid Density (ρ)", f"{density:.4f} kg/m³")
    st.success("Lightning Strike Analysis Complete!")
