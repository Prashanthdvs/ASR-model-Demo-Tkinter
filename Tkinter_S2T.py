import tkinter as tk   
import customtkinter as ctk
import soundfile as sf
import sounddevice as sd
from tkinter import filedialog

# pip install git+https://github.com/openai/whisper.git
# import whisper

# # Select from the following models: "tiny", "base", "small", "medium", "large"
# model = whisper.load_model("base")


from transformers import pipeline
pipe = pipeline(model="Shubham09/whisper31filescheck")    # change to "your-username/the-name-you-picked"

# def transcribe(audio):
#     text = pipe(audio)["text"]
#     return text


# create the app


app = tk.Tk()
app.geometry("540x512")
app.title("Offline Speech to text")
ctk.set_appearance_mode("Dark")
main_label = ctk.CTkLabel(master=app, height=112, width=512, text_color="black",corner_radius=8,fg_color="gray75", font=("Roboto Medium", -16))   #, text_font=("Roboto Medium", -16))
main_label.place(x=10, y=310)
main_label.configure(text="Text")




def voice_rec():
    fs = 16000
    global myrecording
    # seconds
    duration = 5
    main_label.configure(text="Recording...")
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    print(type(myrecording))
    sd.wait()

    # Save as FLAC file at correct sampling rate
    sf.write("my_Audio_file.flac", myrecording, fs)
    main_label.configure(text="Recording done")
    # audio = "my_Audio_file.flac"
    # options = {"fp16": False, "language": None, "task": "transcribe"}
    # results = pipe(audio, **options)
    # print(results["text"])
    # main_label.configure(text=results["text"])

def upload():
    global filename
    filename = filedialog.askopenfilename(filetypes=(('Audio Files','.wav'), ("All Files", "*.*")))
    main_label.configure(text=('Selected:', filename))
    audio = filename
    options = {"fp16": False, "language": None, "task": "transcribe"}
    results = pipe(audio, **options)
    print(results["text"])
    main_label.configure(text=results["text"], wraplength=main_label.winfo_width())


def transcribe():
    if myrecording.size!=0:
        audio = "my_Audio_file.flac"

        # You can provide the language to the model if it is a bit to "exotic" to predict
        options = {"fp16": False, "language": None, "task": "transcribe"}
        results = pipe(audio, **options)

        print(results["text"])
        main_label.configure(text=results["text"])




recordButton = ctk.CTkButton(master=app,
    height=40,
    width=120,
    font=("Roboto Medium", 20),
    text_color="white",
    fg_color=("white", "gray38"),
    command=voice_rec)
recordButton.configure(text="Record")
recordButton.place(x=106, y=60)

transcribeButton = ctk.CTkButton(master=app,
    height=40,
    width=120,
    font=("Roboto Medium", 20),
    text_color="white",
    fg_color=("white", "gray38"),
    command=transcribe,
)
transcribeButton.configure(text="Transcribe")
transcribeButton.place(x=306, y=60)

translateButton = ctk.CTkButton(master=app,
    height=40,
    width=120,
    font=("Roboto Medium", 20),
    text_color="white",
    fg_color=("white", "gray38"),
    command=upload,
)
translateButton.configure(text="Choose File")
translateButton.place(x=106, y=150)


# run app
app.mainloop()
