import streamlit as st
import numpy as np
import pandas as pd
import time

# 1. Page Configuration
st.set_page_config(page_title="Thermodynamics Property Finder", layout="wide")

# 2. Advanced CSS for Turbine, Pipes, and Lightning Borders
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
        padding: 25px;
        border-radius: 15px;
        background: rgba(10, 12, 16, 0.6);
        box-shadow: 0 0 15px rgba(74, 144, 226, 0.4), 
                    inset 0 0 15px rgba(74, 144, 226, 0.2);
        position: relative;
        overflow: hidden;
        margin-bottom: 20px;
        min-height: 480px; /* Aligns both columns nicely */
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

    /* Horizontal Lightning Animation for Calculation */
    @keyframes horizontal-bolt {
        0% { transform: scaleX(0); opacity: 0; }
        50% { transform: scaleX(1); opacity: 1; }
        100% { transform: scaleX(0); opacity: 0; }
    }
    .lightning-horizontal {
        position: relative;
        width: 100%;
        height: 6px;
        background: white;
        box-shadow: 0 0 15px 5px #4a90e2;
        margin-top: 15px;
        margin-bottom: 15px;
        z-index: 10;
        animation: horizontal-bolt 0.4s ease-in-out forwards;
    }

    /* --- Turbine System with Pipes and Steam --- */
    .turbine-container {
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 20px 0;
        position: relative;
    }
    
    .pipe-in {
        width: 40px;
        height: 12px;
        background: linear-gradient(to bottom, #555, #222, #555);
        border: 1px solid #777;
        border-radius: 5px 0 0 5px;
    }

    .turbine-housing {
        width: 70px;
        height: 70px;
        background: #1e2130;
        border: 4px solid #3d4256;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 2;
        box-shadow: 0 0 15px rgba(74, 144, 226, 0.2);
    }

    .turbine-blade {
        font-size: 40px;
        animation: rotate 2s linear infinite;
        color: #d4af37;
    }

    .pipe-out {
        width: 40px;
        height: 12px;
        background: linear-gradient(to bottom, #555, #222, #555);
        border: 1px solid #777;
        border-radius: 0 5px 5px 0;
        position: relative;
    }

    /* Steam Effect */
    .steam-effect {
        position: absolute;
        right: -15px;
        top: -10px;
        font-size: 20px;
        opacity: 0;
        animation: steam-rise 2s infinite;
        color: #ddd;
    }
    
    @keyframes steam-rise {
        0% { transform: translateY(0) scale(0.5); opacity: 0; }
        50% { opacity: 0.8; }
        100% { transform: translateY(-30px) scale(1.5); opacity: 0; }
    }

    @keyframes rotate { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }

    .title-box {
        border: 2px solid #4a90e2;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        background: rgba(74, 144, 226, 0.1);
        margin-bottom: 20px;
    }
    
    /* Styled Round Red Button */
    .stButton>button {
        background: radial-gradient(circle, #ff4b4b 0%, #a50000 100%) !important;
        color: white !important;
        border-radius: 50% !important;
        width: 130px !important;
        height: 130px !important;
        font-weight: bold !important;
        border: 4px solid #1e2130 !important;
        box-shadow: 0 0 15px rgba(255, 75, 75, 0.4) !important;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 25px rgba(255, 75, 75, 0.7) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Header
st.markdown('<div class="title-box"><h1 style="color:#4a90e2; margin:0; font-family:sans-serif;">Thermodynamics Property Finder</h1></div>', unsafe_allow_html=True)
st.write(f"<p style='text-align:center; color:#d4af37; font-size:15px; font-weight:bold; margin-top:-10px;'>Created by: Ramish Ali | Reg. No: 25-ME-87</p>", unsafe_allow_html=True)

# 4. Sidebar with Pipe and Steam
st.sidebar.title("Industrial Dashboard")
st.sidebar.markdown("""
    <div class="turbine-container">
        <div class="pipe-in"></div>
        <div class="turbine-housing">
            <div class="turbine-blade">⚙️</div>
        </div>
        <div class="pipe-out">
            <div class="steam-effect">💨</div>
            <div class="steam-effect" style="animation-delay: 0.5s; right: -25px;">💨</div>
        </div>
    </div>
    <p style="text-align: center; color: #d4af37; font-weight: bold;">LIVE TURBINE CYCLE</p>
    """, unsafe_allow_html=True)
st.sidebar.info("Core Status: Stable")

# 5. Main UI with Columns
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    # Div start for input lighting box
    st.markdown('<div class="lightning-box">', unsafe_allow_html=True)
    st.markdown("### 📥 Input Parameters")
    
    R = st.number_input("Gas Constant R (J/kg-K)", value=287.0, key="gas_r")
    T = st.number_input("Temperature (K)", value=300.0, key="temp_t")
    P = st.number_input("Pressure (Pa)", value=101325.0, key="pres_p")
    
    st.write("##")
    calculate = st.button("CALCULATE")
    
    st.markdown('</div>', unsafe_allow_html=True) # Div end for input lightning box

with col2:
    # Div start for chart lighting box
    st.markdown('<div class="lightning-box">', unsafe_allow_html=True)
    st.markdown("### 📊 P-V Diagram Analysis")
    
    v = np.linspace(0.1, 1.0, 50)
    p = (R * T) / v
    chart_data = pd.DataFrame({'Volume': v, 'Pressure': p}).set_index('Volume')
    st.line_chart(chart_data)
    
    st.markdown('</div>', unsafe_allow_html=True) # Div end for chart lighting box

# 6. Results & Calculations
if calculate:
    st.markdown('<div class="lightning-horizontal"></div>', unsafe_allow_html=True)
    density = P / (R * T)
    st.divider()
    
    # Custom styled metric block for results
    st.markdown(f"""
        <div style="background: rgba(74, 144, 226, 0.1); padding: 20px; border-radius: 10px; border-left: 5px solid #4a90e2;">
            <span style="color: #aaa; font-size: 14px; uppercase; font-weight: bold;">Fluid Density (ρ)</span><br>
            <span style="color: #00f0ff; font-size: 32px; font-weight: bold;">{density:.4f} kg/m³</span>
        </div>
        """, unsafe_allow_html=True)
        
    st.success("Lightning Strike Analysis Complete!")
