import gradio as gr
import soundfile as sf
import sounddevice as sd
from transformers import pipeline

pipe = pipeline(model="Shubham09/whisper31filescheck")     # change to "your-username/the-name-you-picked"    

def sound(audio):
    fs = 16000
    sf.write("new_Audio_file.flac",audio, fs)
    return "new_Audio_file.flac"
def transcribe():
    #audio = "new_Audio_file.flac"
    text = pipe(sound())["text"]
    return text

gr.Interface(
    fn=transcribe, 
    inputs=gr.Audio(source="microphone", type="filepath"), 
    outputs="text").launch()