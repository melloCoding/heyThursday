import ollama
from gtts import gTTS
from playsound import playsound
import os
import time
import speech_recognition as sr
from gtts import gTTS

while True:
  print('ran')
  while True:
    with sr.Microphone() as mic:
        r = sr.Recognizer()
        #r.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
        audio = r.listen(mic)
        text = r.recognize_google(audio)
        text = text.lower()
        if "hey thursday" in text:
          print('hey thirsday recognized')
          audio = r.listen(mic)
          text = r.recognize_google(audio)
          print(text)
          break
        
      #print(r.recognize_google(audio))
  response = ollama.chat(model='llama2', messages=[
    {
     'role': 'user',
     'content': text,
    },
    ])
  print(response['message']['content'])


  tts = gTTS(response['message']['content'])
  tts.save('output.mp3')
  time.sleep(5)
  playsound('output.mp3', block=True)
  os.remove("output.mp3")
