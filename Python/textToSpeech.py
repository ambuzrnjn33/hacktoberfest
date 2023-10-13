from gtts import gTTS
import os

def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang, slow=False)
    filename = "output.mp3"
    tts.save(filename)
    os.system(f"start {filename}")  # On Windows
    # os.system(f"mpg321 {filename}")  # On Linux, you might need to install mpg321

if __name__ == "__main__":
    text = "Hello, how are you?"
    text_to_speech(text)
