import streamlit as st
import numpy as np
import pandas as pd
import time

# 1. Page Configuration
st.set_page_config(page_title="Thermodynamics Property Finder", layout="wide")

# 2. Updated CSS - Replacing boxes with simple horizontal lines
st.markdown("""
    <style>
    /* Background Fix */
    .stApp {
        background-color: #0a0c10;
        background-image: linear-gradient(rgba(10, 12, 16, 0.8), rgba(10, 12, 16, 0.8)),
            url('https://www.transparenttextures.com/patterns/carbon-fibre.png');
    }

    /* Simple Horizontal Line Replacement */
    .horizontal-divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, #4a90e2, transparent);
        margin: 20px 0;
        width: 100%;
    }

    /* Main Container Styling */
    .content-area {
        padding: 20px;
        border-radius: 10px;
        background: rgba(15, 18, 25, 0.5);
    }

    /* Vertical Partition Line */
    .v-partition {
        border-left: 2px solid rgba(74, 144, 226, 0.4);
        height: 450px;
        margin-left: auto;
        margin-right: auto;
    }

    /* Result Styling - Bold */
    .bold-result {
        font-weight: 900 !important;
        font-size: 24px !important;
        color: white !important;
        background-color: #28a745;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        border: 3px solid #1e7e34;
        margin-top: 25px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.4);
    }

    /* Lightning Flash Effect */
    @keyframes lightning-effect {
        0% { width: 0%; opacity: 0; }
        30% { width: 100%; opacity: 1; box-shadow: 0 0 20px #00f0ff; }
        100% { width: 100%; opacity: 0; }
    }
    .lightning-line {
        height: 4px;
        background: white;
        animation: lightning-effect 0.5s ease-out forwards;
        margin-top: 10px;
    }

    /* Red Calculate Button */
    .stButton > button {
        background: radial-gradient(circle, #ff4b4b 0%, #a50000 100%) !important;
        color: white !important;
        width: 100% !important;
        height: 55px !important;
        font-weight: bold !important;
        font-size: 20px !important;
        border-radius: 10px !important;
        text-transform: uppercase;
        border: 2px solid #111 !important;
    }

    .turbine-icon { font-size: 55px; animation: rotate 2s linear infinite; display: inline-block; color: #d4af37; }
    @keyframes rotate { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    </style>
    """, unsafe_allow_html=True)

# 3. Header Section
st.markdown('<h1 style="color:#4a90e2; text-align:center; margin-bottom:0;">Thermodynamics Property Finder</h1>', unsafe_allow_html=True)
st.write(f"<p style='text-align:center; color:#d4af37; font-weight:bold; font-size:18px;'>Created by: Ramish Ali | Reg. No: 25-ME-87</p>", unsafe_allow_html=True)

# 4. Simple Horizontal Line (Replacing the blue box)
st.markdown('<div class="horizontal-divider"></div>', unsafe_allow_html=True)

# 5. Sidebar
st.sidebar.title("Industrial Dashboard")
st.sidebar.markdown('<div style="text-align:center; margin-top:30px;"><div class="turbine-icon">⚙️</div><p style="color:#d4af37; font-weight:bold; font-size:20px;">TURBINE ACTIVE</p></div>', unsafe_allow_html=True)

# 6. Main UI Layout
st.markdown('<div class="content-area">', unsafe_allow_html=True)
col1, mid, col2 = st.columns([1, 0.1, 1])

with col1:
    st.markdown("### 📥 Input Parameters")
    r_val = st.number_input("Gas Constant R (J/kg-K)", value=287.0)
    t_val = st.number_input("Temperature (K)", value=300.0)
    p_val = st.number_input("Pressure (Pa)", value=101325.0)
    st.write("##")
    calc_button = st.button("CALCULATE")
    flash_space = st.empty()

with mid:
    # Drawing the Vertical Partition Line
    st.markdown('<div class="v-partition"></div>', unsafe_allow_html=True)

with col2:
    st.markdown("### 📊 P-V Diagram Analysis")
    v_arr = np.linspace(0.1, 1.0, 50)
    p_arr = (r_val * t_val) / v_arr
    chart_df = pd.DataFrame({'Volume': v_arr, 'Pressure': p_arr}).set_index('Volume')
    st.line_chart(chart_df, use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# 7. Logic & Results
if calc_button:
    # Trigger Flash Light
    flash_space.markdown('<div class="lightning-line"></div>', unsafe_allow_html=True)
    time.sleep(0.2)
    
    # Calculate Density
    density_res = p_val / (r_val * t_val)
    
    # Show Bold Result
    st.markdown(f"""
        <div class="bold-result">
            ANALYSIS COMPLETE! FLUID DENSITY: {density_res:.4f} kg/m³
        </div>
    """, unsafe_allow_html=True)
