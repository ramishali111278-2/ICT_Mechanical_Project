# Is function ko play_steam_sound se replace kar den
def play_steam_sound():
    # Direct reliable link
    sound_url = "https://www.soundjay.com/mechanical/sounds/steam-engine-inner-workings-1.mp3"
    
    # Humne 'controls' add kiye hain taake aap manually bhi check kar saken
    audio_html = f"""
        <div style="display:none;">
            <audio id="steamAudio" autoplay>
                <source src="{sound_url}" type="audio/mp3">
            </audio>
        </div>
        <script>
            var audio = document.getElementById("steamAudio");
            audio.play();
        </script>
    """
    st.markdown(audio_html, unsafe_allow_html=True)
