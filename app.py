import streamlit as st
import time

# Sidebar aur Page Config (Taake interface maintain rahe)
st.set_page_config(page_title="Steam Calc", layout="centered")

with st.sidebar:
    st.header("Settings")
    st.write("Yahan aapka side panel wapas aa gaya!")

st.title("Thermodynamic Calculator")

# Inputs
pressure = st.number_input("Enter Pressure (bar):", min_value=0.1, value=1.0)
temperature = st.number_input("Enter Temperature (°C):", min_value=0.0, value=100.0)

if st.button("Calculate"):
    # REVISED Smoke Animation (Non-intrusive)
    smoke_animation = """
    <div class="steam-box">
        <div class="steam-particle s1"></div>
        <div class="steam-particle s2"></div>
        <div class="steam-particle s3"></div>
    </div>
    <style>
    /* Container ko main body ke peeche rakha hai */
    .steam-box {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: -1; /* Is se background mein chala jayega, buttons gayab nahi honge */
        pointer-events: none;
        background-color: transparent;
    }
    .steam-particle {
        position: absolute;
        bottom: -100px;
        background: rgba(255, 255, 255, 0.2);
        border-radius: 50%;
        filter: blur(30px);
        animation: steamRise 4s infinite ease-out;
    }
    .s1 { width: 200px; height: 200px; left: 20%; animation-delay: 0s; }
    .s2 { width: 300px; height: 300px; left: 50%; animation-delay: 1s; }
    .s3 { width: 250px; height: 250px; left: 70%; animation-delay: 0.5s; }

    @keyframes steamRise {
        0% { transform: translateY(0) scale(1); opacity: 0; }
        50% { opacity: 0.4; }
        100% { transform: translateY(-120vh) scale(2); opacity: 0; }
    }
    </style>
    """
    
    # Animation display
    smoke_placeholder = st.markdown(smoke_animation, unsafe_allow_html=True)
    
    with st.spinner("Steam Generating..."):
        time.sleep(3)
        result = pressure * temperature 
        
    smoke_placeholder.empty() # Animation khatam
    
    st.success("Calculation Done!")
    st.metric(label="Calculated Output", value=f"{result} kJ/kg")
