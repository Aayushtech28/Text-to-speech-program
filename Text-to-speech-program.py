from gtts import gTTS 
import os 
  
def text_to_speech(text, file_name): 
    tts = gTTS(text=text, lang='en') 
    tts.save(file_name) 
  
text = input("Enter text to convert to speech: ") 
file_name = "output.mp3" 
text_to_speech(text, file_name) 
  
os.system("start output.mp3") 
