import streamlit as st
import numpy as np
import pandas as pd

# Page setup
st.set_page_config(page_title="Thermodynamics Property Finder", layout="wide")

# Custom CSS for Professional Industrial Look
st.markdown("""
    <style>
    /* Background with Industrial Grid Pattern */
    .stApp {
        background-color: #0e1117;
        background-image: radial-gradient(#2c303d 1px, transparent 1px);
        background-size: 30px 30px;
    }
    
    /* Header Section (Profile) */
    .user-header {
        background: rgba(45, 49, 66, 0.8);
        border-left: 5px solid #d4af37;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 25px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    .user-name {
        color: #ffffff;
        font-size: 22px;
        font-weight: bold;
        margin: 0;
    }
    .user-roll {
        color: #d4af37;
        font-size: 18px;
        margin: 0;
    }

    /* Professional Circular Button (No Balloons) */
    .stButton>button {
        background: radial-gradient(circle, #ff4b4b 0%, #a50000 100%);
        color: white;
        border-radius: 50%;
        width: 140px;
        height: 140px;
        border: 4px solid #3d4256;
        font-weight: bold;
        font-size: 18px;
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.5);
        margin: 0 auto;
        display: block;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.05) translateY(-5px);
        box-shadow: 0 12px 25px rgba(255, 75, 75, 0.4);
        border-color: #ffffff;
    }
    
    /* Results Box */
    .result-box {
        background-color: #1e2130;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #3d4256;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 1. User Profile Section
st.markdown("""
    <div class="user-header">
        <p class="user-name">Name: Ramish Ali</p>
        <p class="user-roll">Roll Number: 25-ME-87</p>
    </div>
    """, unsafe_allow_html=True)

# 2. Main Title
st.markdown("<h1 style='text-align: center; color: #ffffff; font-family: sans-serif;'>Thermodynamics Property Finder</h1>", unsafe_allow_html=True)

st.write("##")

# 3. Layout: Input Controls and Graphs
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("### 📥 Input Parameters")
    R = st.number_input("Gas Constant R (J/kg-K)", value=287.0, step=0.1)
    T = st.number_input("Temperature (K)", value=300.0, step=0.1)
    P = st.number_input("Pressure (Pa)", value=101325.0, step=1.0)
    
    st.write("##")
    # Industrial Button
    calculate = st.button("CALCULATE")

with col2:
    st.markdown("### 📈 P-V Diagram Analysis")
    # P-V Curve Generation
    v_range = np.linspace(0.1, 1.5, 100)
    p_range = (R * T) / v_range 
    
    df = pd.DataFrame({'Volume (m³)': v_range, 'Pressure (Pa)': p_range})
    st.line_chart(df.set_index('Volume (m³)'))

# 4. Results Logic (Balloons hata diye gaye hain)
if calculate:
    density = P / (R * T)
    spec_vol = 1 / density
    
    st.markdown('<div class="result-box">', unsafe_allow_html=True)
    st.subheader("📊 Calculation Results")
    res1, res2 = st.columns(2)
    res1.metric("Density (ρ)", f"{density:.4f} kg/m³")
    res2.metric("Spec. Volume (v)", f"{spec_vol:.4f} m³/kg")
    st.info("Calculations completed successfully based on Ideal Gas Law.")
    st.markdown('</div>', unsafe_allow_html=True)

# Sidebar with Status
st.sidebar.title("🛠️ Control Panel")
st.sidebar.markdown("---")
st.sidebar.write("**System Status:**")
st.sidebar.success("Engine Online 🟢")
st.sidebar.write("**Simulation Progress:**")
st.sidebar.progress(100)
