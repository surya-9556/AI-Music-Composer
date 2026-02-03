import music21
import numpy as np
import io
from scipy.io.wavfile import write as wav_write
from synthesizer import Synthesizer, Waveform
from src.app.common import CustomException, logger

logger = logger.get_logger(__name__)
c_exception = CustomException.CustomException


def note_to_frequency(note_list):
    try:
        logger.info('Creating frequencies from note list.....')
        freq = []
        for str_node in note_list:
            try:
                note = music21.note.Note(str_node)
                freq.append(note.pitch.frequency)
            except Exception as e:
                # error_message = c_exception("Unable to Extract the correct frequenct from note list", e)
                # logger.error(str(error_message))
                continue
        logger.info(f"Succuessfully converted and appended the notes to frequencies and length is {len(freq)}")

        return freq
    except Exception as e:
        error_message = c_exception("Unable to add the frequency to the list", e)
        logger.error(str(error_message))
        return None
    
def generate_wav_bytes_from_notes_freq(notes):
    try:
        logger.info('Creating the synthesizer files from the converted note from music21.......')
        synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False) ### osc => oscilation
        sample_rate = 44100 ### standard wav file rate

        audio = np.concatenate([synth.generate_constant_wave(freq, 0.5) for freq in notes])

        buffer = io.BytesIO()
        wav_write(buffer,sample_rate, audio.astype(np.float32))

        logger.info("Successfully converted the notes and generated synthesized audio data and stored in buffer.....")
        return buffer.getvalue()
    except Exception as e:
        error_message = c_exception("Unable to generate the synthesizers from notes", e)
        logger.error(str(error_message))
        return None