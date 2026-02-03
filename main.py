import streamlit as st
from src.app.app import MusicClass
from src.app.utils import *
from src.app.common import CustomException, logger
from io import BytesIO
from dotenv import load_dotenv

logger = logger.get_logger(__name__)
c_exception = CustomException.CustomException

st.set_page_config(page_title="Music Composer", layout="centered")
st.title("AI Music Composer")
st.markdown("Generate AI music by describing the style and content.....")

music_input = st.text_input("Describe the music you want to compose..")
style = st.selectbox("Choose a style..",["Sad","Happy","Jazz","Romantic"])

if st.button("Generate Music") and music_input:
    generator = MusicClass()

    with st.spinner("Generating music.."):
        melody = generator.generate_melody(music_input)
        harmony = generator.generate_harmony(melody)
        rythm = generator.generate_rythm(melody)

        composition = generator.adapt_style(style,melody,harmony,rythm)

        melody_notes = melody.split()
        mel_freq = note_to_frequency(melody_notes)

        har_chords = harmony.split()
        har_notes = []
        for chord in har_chords:
            har_notes.extend(chord.split('-'))

        har_freq = note_to_frequency(har_notes)

        all_freq = mel_freq+har_freq

        wav_bytes = generate_wav_bytes_from_notes_freq(all_freq)

    st.audio(BytesIO(wav_bytes),format='audio/wav')

    st.success("Music generated successfully.....!!!!!")

    with st.expander("Composition Summary"):
        st.text(composition)