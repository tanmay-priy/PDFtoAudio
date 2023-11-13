
import os
import gradio as gr
import tempfile
from PyPDF2 import PdfReader
from gtts import gTTS
import tempfile

def pdf_to_audio(pdf_file):
    # Read PDF file
    with open(pdf_file.name, 'rb') as f:
        pdf_reader = PdfReader(f)
        text = ""
        for page in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page].extract_text()
    
    # Convert text to audio
    audio_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts = gTTS(text=text, lang='en')
    tts.save(audio_file.name)
    
    # Return audio file
    return audio_file.name

iface = gr.Interface(fn=pdf_to_audio, inputs="file", outputs="audio", title="PDF to Audio Converter")
iface.launch()

